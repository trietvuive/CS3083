from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import customer
from datetime import datetime

# Add a new route /customer/register to cust_auth blueprint
@customer.route('/view_flights/', methods = ['GET','POST'])
def view_flights():
    if 'customer_email' not in session:
        return redirect(url_for('customer.login'))
    
    if request.method == 'POST':
        from_date = datetime.strptime(request.form['From'],'%m/%d/%Y').strftime('%Y-%m-%d')
        to_date = datetime.strptime(request.form['To'],'%m/%d/%Y').strftime('%Y-%m-%d')
        print(from_date, to_date)
    return render_template('flight/view_flight_table.html')
