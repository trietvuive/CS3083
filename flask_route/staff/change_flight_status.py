from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import staff

# Add a new route /customer/register to cust_auth blueprint
@staff.route('/change_flight', methods = ['GET','POST'])
def change_flight_status():
    if 'staff_username' not in session:
        return redirect(url_for('staff.login'))
    
    status = None
    error = False
    if request.method == 'POST':
        # get all POST values
        name = request.form['Airplane Name']
        departure = request.form['Departure Date']
        flight_num = request.form['Flight Number']
        status = request.form['Status']
        
        # cust_reg_veri_query checks if the email is in the Customer table
        cursor = conn.cursor()
        # query not done yet
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
    return render_template('staff/change_flight.html', status = status, error = error)
