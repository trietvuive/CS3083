from flask import render_template, Blueprint, request
from route import customer

@customer.route('/home')
def home():
    return render_template('hello.html', email = request.args.get('name'))
