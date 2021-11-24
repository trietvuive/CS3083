from flask import Flask, render_template, session, redirect, url_for, request, escape
import pymysql
import hashlib
from flask_route.root.hello_world import home
import flask_route.customer.cust_login
import flask_route.customer.cust_register
from flask_route.customer.cust_home import cust_home
import settings
from route import *

app = Flask(__name__)
app.register_blueprint(home, url_prefix = '/')
app.register_blueprint(cust_auth, url_prefix = '/customer')
app.register_blueprint(cust_home, url_prefix = '/customer')

if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)
