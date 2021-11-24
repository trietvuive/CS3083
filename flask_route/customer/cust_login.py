from flask import render_template, redirect, url_for, Blueprint, request
from settings import *
from route import cust_auth
import pymysql

@cust_auth.route('/login', methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['Email']
        password = md5(request.form['Password'])
        cursor = conn.cursor()
        cursor.execute(cust_log_veri_query, (email, password))

        data = cursor.fetchone()
        cursor.close()
        if not data:
            error = 'Invalid Credentials...'
        else:
            return redirect(url_for('cust_home.home', name = email))
    return render_template('customer_login.html', error = error)

