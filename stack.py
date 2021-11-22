from flask import Flask, render_template, session, redirect, url_for, request, escape
import pymysql
import hashlib
from flask_route.hello_world import home
from flask_route.customer import customer

conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'trietrie',
                       db='CS3083',
                       charset = 'utf8mb4',
                       cursorclass = pymysql.cursors.DictCursor)

app = Flask(__name__)
app.register_blueprint(home, url_prefix = '/')
app.register_blueprint(customer, url_prefix = '/customer')

if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)

