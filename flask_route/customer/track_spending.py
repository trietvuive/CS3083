from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import customer
import datetime

# Add a new route /customer/register to cust_auth blueprint
@customer.route('/track_spending', methods = ['GET','POST'])
def track_spending():
    if 'customer_email' not in session:
        return redirect(url_for('customer.login'))

    customer_email = session['customer_email']
    
    cursor = conn.cursor()
    cursor.execute(cust_spent_year, (customer_email))
    year_spending = cursor.fetchone()['sum']
    print(year_spending)

    
    if request.method == 'POST':
        from_date = datetime.datetime.strptime(request.form['From'],'%m/%d/%Y').strftime('%Y-%m-%d')
        to_date = datetime.datetime.strptime(request.form['To'],'%m/%d/%Y').strftime('%Y-%m-%d')
        cursor.execute(cust_spent_monthly_range, (customer_email, from_date, to_date))
    else:
        cursor.execute(cust_spent_monthly_sixmonths, (customer_email))
    records = cursor.fetchall()
    cursor.close()
    return render_template('flight/customer_spending.html', flights = records, sum = year_spending)
