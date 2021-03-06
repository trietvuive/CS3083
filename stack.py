from flask import Flask, render_template
import pymysql
import hashlib
import settings

from flask_route.root import root, check_status, search_flight
from flask_route.customer import cust_login, cust_register, cust_home, create_order, view_flights, add_comment, track_spending
from flask_route.staff import staff_login, staff_register, staff_home, create_new_airport, change_flight_status
from flask_route.staff import create_airplane, create_flight, view_flights, view_avg_rating, view_customers, view_report, view_revenue, view_destination
from route import *

# we'll split the big Flask file into smaller files using Blueprint
# Each route has its own blueprint import from route.py
# Each file will implement the route import from route.py

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(home, url_prefix = '/')
app.register_blueprint(customer, url_prefix = '/customer')
app.register_blueprint(flights, url_prefix = '/flights')
app.register_blueprint(staff, url_prefix = '/staff')

@app.errorhandler(404)
def invalid_route(e):
    return render_template('root/404.html')

@app.errorhandler(500)
def internal_error(e):
    return render_template('root/503.html')

if __name__ == "__main__":
    #127.0.0.1 is localhost
    app.run('127.0.0.1', 5000, debug = True)
