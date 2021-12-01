from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import staff

# Add a new route /customer/register to cust_auth blueprint
@staff.route('/create_flight', methods = ['GET','POST'])
def create_flight():
    if 'staff_username' not in session:
        return redirect(url_for('staff.login'))
    
    status = None
    error = False
    if request.method == 'POST':
        # get all POST values
        insert_post_tuple = create_POST_tuple(['Airline','Airplane Brand','Airplane ID',
                                        'Arrival Airport', 'Arrival Date', 'Base Price',
                                        'Departure Airport', 'Departure Date', 'Flight Number','Status'],request.form)

        verify_tuple = create_POST_tuple(['Airline', 'Departure Date', 'Flight Number'], request.form)
        
        cursor = conn.cursor()
        # cursor.execute(staff_reg_veri_query, (username))
        data = cursor.fetchone()

        if data:
            status = 'This airport already exists'
        else:
            try:
                # cursor.execute(staff_ins_query, (username, pwd, airline, first_name, last_name, dob))
                conn.commit()
                status = 'Registered =)'
                error = False
            except:
                status = 'Error...=('
                error = True
        cursor.close()
    return render_template('staff/create_flight.html', status = status, error = error)
