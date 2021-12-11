from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import staff
import datetime

# Add a new route /customer/register to cust_auth blueprint
@staff.route('/view_frequent_customer/', methods = ['GET','POST'])
def view_frequent_customer():
    if 'staff_username' not in session:
        return redirect(url_for('staff.login'))

    cursor = conn.cursor()
    airline_name = session['staff_airline']
    cursor.execute(staff_show_freq_customer, (airline_name))
    records = cursor.fetchall()
    cursor.close()
    return render_template('flight/view_frequent_customers.html', customers = records)

@staff.route('/view_customer/')
def view_customer():
    if 'staff_username' not in session:
        return redirect(url_for('staff.login'))
    flights = {}
    if 'cust_email' in request.args:
        cust_email = request.args['cust_email']
        airline_name = session['staff_airline']
        cursor = conn.cursor()
        cursor.execute(staff_show_customer_flights, (cust_email, airline_name))
        flights = cursor.fetchall()
        cursor.close()

    
    return render_template('flight/view_customer.html', flights = flights)
