from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import customer

# Add a new route /customer/register to cust_auth blueprint
@customer.route('/add_comment', methods = ['GET','POST'])
def add_comment():
    if 'customer_email' not in session:
        return redirect(url_for('customer.cust_login'))
    status = None
    error = False
    if request.method == 'POST':
        # get all POST values

        email = session['customer_email']
        airline = request.form['Flight Airline']
        flight_num = request.form['Flight Number']
        rating = request.form['Rating']
        departure_date = request.form['Departure Date']
        
        # cust_reg_veri_query checks if the email is in the Customer table
        cursor = conn.cursor()
        cursor.execute(cust_reg_veri_query, (request.form['Email']))
        data = cursor.fetchone()

        if data:
            status = 'This user already exists'
        else:
            try:
                cursor.execute(cust_ins_query, post_tuple)
                conn.commit()
                status = 'Registered =)'
                error = False
            except:
                status = 'Error...=('
                error = True
        cursor.close()
    return render_template('customer/add_comment.html', status = status, error = error)
