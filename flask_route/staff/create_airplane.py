from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import staff

# Add a new route /customer/register to cust_auth blueprint
@staff.route('/create_airplane', methods = ['GET','POST'])
def create_airplane():
    if 'staff_username' not in session:
        return redirect(url_for('staff.login'))
    
    status = None
    error = False
    if request.method == 'POST':
        # get all POST values
        airline = request.form['Airline']
        ID = request.form['ID']
        airplane_number = request.form['Airplane Number']


        cursor = conn.cursor()
        cursor.execute(staff_reg_veri_query, (username))
        data = cursor.fetchone()

        if data:
            status = 'This airport already exists'
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
    return render_template('staff/create_airplane.html', status = status, error = error)
