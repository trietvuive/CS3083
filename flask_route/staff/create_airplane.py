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
        post_tuple = create_POST_tuple(['Airline Name','ID','Number Of Seats'], request.form)
        cursor = conn.cursor()
        
        try:
            cursor.execute(staff_ins_airplane, post_tuple)
            conn.commit()
            status = 'Registered =)'
            error = False
        except Exception as e:
            status = e
            error = True
        cursor.close()
    return render_template('staff/create_airplane.html', status = status, error = error)
