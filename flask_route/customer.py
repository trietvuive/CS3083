from flask import render_template, redirect, url_for, Blueprint, request
import pymysql
import hashlib

cust_log_veri_query = 'SELECT * FROM Users WHERE username = %s AND password = %s'
cust_reg_veri_query = 'SELECT * FROM Customer WHERE email = %s'
cust_ins_query = 'INSERT INTO Customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'trietrie',
                       db='CS3083',
                       charset = 'utf8mb4',
                       cursorclass = pymysql.cursors.DictCursor)

customer = Blueprint('customer', __name__)                    
@customer.route('/login', methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['Email']
        print(username)
        password = md5(request.form['Password'])
        cursor = conn.cursor()
        cursor.execute(cust_log_veri_query, (username, password))

        data = cursor.fetchone()
        cursor.close()
        if not data:
            error = 'Invalid Credentials...'
        else:
            return redirect(url_for('hello', name = username))
    return render_template('customer_login.html', error = error)

@customer.route('/register', methods = ['GET','POST'])
def register():
    status = None
    if request.method == 'POST':
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
        
        cursor = conn.cursor()
        cursor.execute(cust_reg_veri_query, (email))
        data = cursor.fetchone()

        if data:
            status = 'This user already exists'
        else:
            #Todo: Red error if transaction failed
            cursor.execute(cust_ins_query, (email, pwd, name, building_no, add_street, add_city, add_state,
                                            phone_no, passport_num, passport_exp, passport_country, dob))
            conn.commit()
            status = 'Registered =)'
        cursor.close()
    return render_template('customer_register.html', status = status)
