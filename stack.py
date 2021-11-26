from flask import Flask
import pymysql
import hashlib
import settings

from flask_route.root import root, flights
from flask_route.customer import cust_login, cust_register, cust_home

from route import *

# we'll split the big Flask file into smaller files using Blueprint
# Each route has its own blueprint import from route.py
# Each file will implement the route import from route.py

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(home, url_prefix = '/')
app.register_blueprint(customer, url_prefix = '/customer')
app.register_blueprint(flights, url_prefix = '/flights')

if __name__ == "__main__":
    #127.0.0.1 is localhost
    app.run('127.0.0.1', 5000, debug = True)
