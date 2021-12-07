from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import staff
import datetime

# Add a new route /customer/register to cust_auth blueprint
@staff.route('/view_destination/', methods = ['GET','POST'])
def view_destination():
    if 'staff_username' not in session:
        return redirect(url_for('staff.login'))

    airline_name = session['staff_airline']
    cursor = conn.cursor()
    cursor.execute(staff_top_destinations_month, (airline_name))
    month = cursor.fetchall()

    cursor.execute(staff_top_destinations_year, (airline_name))
    year = cursor.fetchall()

    cursor.close()
    print(airline_name, month)
    print(year)
    
    
    return render_template('flight/view_destination.html', month = month, year = year)


