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
        email = request.form['Email']
        pwd = md5(request.form['Password'])
        name = request.form['Name']
        building_no = request.form['Building Number']
        add_street = request.form['Address Street']
        add_city = request.form['Address City']
        add_state = request.form['Address State']
        phone_no = request.form['Phone Number']
        passport_num = request.form['Passport Number']
        passport_exp = request.form['Passport Expiration']
        passport_country = request.form['Passport Country']
        dob = request.form['Date Of Birth']

        # cust_reg_veri_query checks if the email is in the Customer table
        cursor = conn.cursor()
        cursor.execute(cust_reg_veri_query, (email))
        data = cursor.fetchone()

        if data:
            status = 'This user already exists'
        else:
            try:
                cursor.execute(cust_ins_query, (email, pwd, name, building_no, add_street, add_city, add_state,
                                            phone_no, passport_num, passport_exp, passport_country, dob))
                conn.commit()
                status = 'Registered =)'
                error = False
            except:
                status = 'Error...=('
                error = True
        cursor.close()
    return render_template('customer/customer_register.html', status = status, error = error)
