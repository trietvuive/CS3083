from flask import render_template, redirect, url_for, Blueprint, request, session
from settings import *
from route import staff
import pymysql

@staff.route('/login', methods = ['GET','POST'])
def login():
    if 'staff_username' in session:
        return redirect(url_for('staff.home', name = session['staff_username']))
    error = None
    if request.method == 'POST':
        username = request.form['Username']
        password = md5(request.form['Password'])
        cursor = conn.cursor()
        cursor.execute(staff_log_veri_query, (username, password))

        data = cursor.fetchone()
        cursor.close()
        if not data:
            error = 'Invalid Credentials...'
        else:
            session['staff_username'] = username
            return redirect(url_for('staff.home', name = username))
    return render_template('staff/staff_login.html', error = error)


