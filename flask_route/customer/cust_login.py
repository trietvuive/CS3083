from flask import render_template, redirect, url_for, Blueprint, request, session
from settings import *
from route import customer
import pymysql

@customer.route('/login', methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['Email']
        password = md5(request.form['Password'])
        cursor = conn.cursor()
        cursor.execute(cust_log_veri_query, (email, password))

        data = cursor.fetchone()
        cursor.close()
        if not data and not development:
            error = 'Invalid Credentials...'
        else:
            session['customer_email'] = email
            return redirect(url_for('customer.home'))
    return render_template('customer/customer_login.html', error = error)


