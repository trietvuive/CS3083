from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import staff

# Add a new route /customer/register to cust_auth blueprint
@staff.route('/create_airport', methods = ['GET','POST'])
def create_airport():
    if 'staff_username' not in session:
        return redirect(url_for('staff.login'))
    
    status = None
    error = False
    if request.method == 'POST':
        # get all POST values
        post_tuple = create_POST_tuple(['City','Code','Name'], request.form)
        cursor = conn.cursor()

        try:
            cursor.execute(staff_ins_airport, post_tuple)
            conn.commit()
            status = 'Registered =)'
            error = False
        except Exception as e:
            print(e)
            status = e
            error = True
        cursor.close()
    return render_template('staff/create_airport.html', status = status, error = error)
