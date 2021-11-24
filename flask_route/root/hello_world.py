from flask import Blueprint, render_template
from route import home

@home.route('/')
def hello_world():
    return "<p> Hello, World! </p>"
@home.route('/flights')
def search_flight():
    return render_template('search_flight.html')
