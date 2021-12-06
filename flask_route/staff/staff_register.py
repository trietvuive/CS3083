from flask import render_template, redirect, url_for, Blueprint, request
import pymysql
import hashlib
from settings import *
from route import staff

@staff.route('/register', methods = ['GET','POST'])
def register():
    status = None
    error = False
    if request.method == 'POST':
        # get all POST values
        username = request.form['Username']
        pwd = md5(request.form['Password'])
        first_name = request.form['First Name']
        last_name = request.form['Last Name']
        airline = request.form['Airline']
        dob = request.form['Date Of Birth']

        # cust_reg_veri_query checks if the email is in the Customer table
        cursor = conn.cursor()
        cursor.execute(staff_reg_veri_query, (username))
        data = cursor.fetchone()

        if data:
            status = 'This user already exists'
        else:
            try:
                cursor.execute(staff_ins_query, (username, pwd, airline, first_name, last_name, dob))
                conn.commit()
                status = 'Registered =)'
                error = False
            except:
                status = 'Error...=('
                error = True
        cursor.close()
    return render_template('staff/staff_register.html', status = status, error = error)
