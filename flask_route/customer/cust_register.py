from flask import render_template, redirect, url_for, Blueprint, request
import pymysql
import hashlib
from settings import *
from route import customer

# Add a new route /customer/register to cust_auth blueprint
@customer.route('/register', methods = ['GET','POST'])
def register():
    status = None
    error = False
    if request.method == 'POST':
        # get all POST values
        post_tuple = create_POST_tuple(['Email','Password','Name','Building Number',
                                        'Address Street', 'Address City', 'Address State',
                                        'Phone Number', 'Passport Number', 'Passport Expiration',
                                        'Passport Country','Date Of Birth'], request.form)

        # cust_reg_veri_query checks if the email is in the Customer table
        cursor = conn.cursor()
        cursor.execute(cust_reg_veri_query, (request.form['Email']))
        data = cursor.fetchone()

        if data:
            status = 'This user already exists'
        else:
            try:
                cursor.execute(cust_ins_query, post_tuple)
                conn.commit()
                status = 'Registered =)'
                error = False
            except:
                status = 'Error...=('
                error = True
        cursor.close()
    return render_template('customer/customer_register.html', status = status, error = error)
