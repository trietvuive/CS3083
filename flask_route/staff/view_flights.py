from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import staff
import datetime

# Add a new route /customer/register to cust_auth blueprint
@staff.route('/view_flights/', methods = ['GET','POST'])
def view_flights():
    if 'staff_username' not in session:
        return redirect(url_for('staff.login'))

    cursor = conn.cursor()
    airline_name = session['staff_airline']
    if request.method == 'POST':
        from_date = datetime.datetime.strptime(request.form['From'],'%m/%d/%Y').strftime('%Y-%m-%d')
        to_date = datetime.datetime.strptime(request.form['To'],'%m/%d/%Y').strftime('%Y-%m-%d')
        cursor.execute(staff_show_flights_range, (from_date, to_date, airline_name))
    else:
        cursor.execute(staff_show_flights_30days, (airline_name))
    records = cursor.fetchall()
    cursor.close()
    print(records)
    return render_template('flight/view_flight_table_staff.html', flights = records)

@staff.route('/view_particular_flights/')
def view_particular_flight():
    if 'staff_username' not in session:
        return redirect(url_for('staff.login'))

    flight_num = request.args['flight_number']
    depart_date = request.args['depart_date']
    airline_name = session['staff_airline']
    cursor = conn.cursor()
    cursor.execute(staff_show_customers, (airline_name, flight_num, depart_date))
    customers = cursor.fetchall()
    print(customers)
    
    return render_template('flight/customer_table.html', customers = customers)
