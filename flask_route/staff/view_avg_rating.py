from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import staff
import datetime

@staff.route('/view_ratings/', methods = ['GET','POST'])
def view_ratings():
    if 'staff_username' not in session:
        return redirect(url_for('staff.login'))

    cursor = conn.cursor()
    airline_name = session['staff_airline']
    cursor.execute(staff_show_avg_rating, (airline_name))
    records = cursor.fetchall()
    cursor.close()
    print(records)
    return render_template('flight/view_flight_avg_rating.html', flights = records)

@staff.route('/view_ratings/flight/')
def view_customer_review():
    if 'staff_username' not in session:
        return redirect(url_for('staff.login'))

    flight_num = request.args['flight_number']
    depart_date = request.args['depart_date']
    airline_name = session['staff_airline']
    cursor = conn.cursor()
    cursor.execute(staff_show_ratings_comments, (airline_name, flight_num, depart_date))
    customers = cursor.fetchall()
    print(customers)
    cursor.close()
    
    return render_template('flight/review_table.html', customers = customers)
