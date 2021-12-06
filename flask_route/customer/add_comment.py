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
        review = request.form['Review']
        depart = request.form['Departure Date']
        
        # cust_reg_veri_query checks if the email is in the Customer table
        cursor = conn.cursor()
        cursor.execute(cust_takes_veri, (email, airline, flight_num, depart))
        data = cursor.fetchone()
        print("Preparing...")
        if not data:
            error = True
            status = "No records found..."
        else:
            try:
                cursor.execute(cust_rate_comment, (review, rating, email, airline, flight_num, depart))
                conn.commit()
                status = 'Thanks for your feedback =)'
                error = False
            except Exception as e:
                print(e)
                status = e
                error = True
        cursor.close()
    return render_template('customer/add_comment.html', status = status, error = error)
