from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import staff
import datetime

# Add a new route /customer/register to cust_auth blueprint
@staff.route('/view_reports/', methods = ['GET','POST'])
def view_reports():
    if 'staff_username' not in session:
        return redirect(url_for('staff.login'))

    cursor = conn.cursor()
    records = []
    if 'From' in request.args and 'To' in request.args:
        from_date = datetime.datetime.strptime(request.args['From'],'%m/%d/%Y').strftime('%Y-%m-%d')
        to_date = datetime.datetime.strptime(request.args['To'],'%m/%d/%Y').strftime('%Y-%m-%d')
        airline_name = session['staff_airline']
        cursor.execute(staff_monthwise_tickets_sold, (from_date, to_date, airline_name))
        records = cursor.fetchall()
        cursor.close()
    return render_template('flight/view_reports.html', tickets = records)


