from flask import render_template, redirect, url_for, Blueprint, request
import pymysql
import hashlib
from settings import *
from route import customer

# Add a new route /customer/register to cust_auth blueprint
@customer.route('/create_order/', methods = ['GET','POST'])
def create_order():
    flight_number = request.args['flight_number']
    airline = request.args['airline']
    depart_date = request.args['depart_date']
    
    print(flight_number, airline, depart_date)
    return render_template('customer/customer_home.html')
