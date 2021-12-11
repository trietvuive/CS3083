from flask import render_template, redirect, url_for, Blueprint, request, session
from settings import *
from route import staff
import pymysql

@staff.route('/login', methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['Username']
        password = md5(request.form['Password'])
        cursor = conn.cursor()
        cursor.execute(staff_log_veri_query, (username, password))
        data = cursor.fetchone()
        print(data)

        cursor.execute(staff_airline, (username))
        airline = cursor.fetchone()
        
        cursor.close()
        if not data and not development:
            error = 'Invalid Credentials...'
        else:
            session['staff_username'] = username
            session['staff_airline'] = airline['airline'] if airline is not None else "China Eastern"
                
            return redirect(url_for('staff.home'))
    return render_template('staff/staff_login.html', error = error)


