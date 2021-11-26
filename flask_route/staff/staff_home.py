from flask import render_template, Blueprint, request
from route import staff

@staff.route('/home')
def home():
    return render_template('hello.html', email = request.args.get('name'))
