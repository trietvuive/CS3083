from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import staff
import datetime

# Add a new route /customer/register to cust_auth blueprint
@staff.route('/view_revenue/', methods = ['GET','POST'])
def view_revenue():
    if 'staff_username' not in session:
        return redirect(url_for('staff.login'))

    cursor = conn.cursor()
    airline = session['staff_airline']
    cursor.execute(staff_revenue_month, (airline))
    month_revenue = int(cursor.fetchone()['sum'])

    cursor.execute(staff_revenue_year, (airline))
    year_revenue = int(cursor.fetchone()['sum'])

    
    
    
    return render_template('staff/staff_revenue.html', year = year_revenue, month = month_revenue)


