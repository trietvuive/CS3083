from flask import render_template, Blueprint, request
from route import cust_home

@cust_home.route('/home')
def home():
    return render_template('hello.html', name = request.args.get('name'))
