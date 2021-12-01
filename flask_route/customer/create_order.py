from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import customer

# Add a new route /customer/register to cust_auth blueprint
@customer.route('/create_order/', methods = ['GET','POST'])
def create_order():
    if 'customer_email' not in session:
        return redirect(url_for('customer.login'))

    flight_number = request.args['flight_number']
    airline = request.args['airline']
    depart_date = request.args['depart_date']
    
    if request.method == 'POST':
        post_tuple = create_POST_tuple(['paymentMethod', 'cardNumber', 'cardDate', 'cvv'],request.form)
        print(post_tuple)
        

    
    return render_template('customer/payment.html', description = 'HOU To LGA', price = '1030')
