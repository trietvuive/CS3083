from flask import Blueprint, render_template, request
from route import home
from settings import *
import pymysql

@home.route('/')
def hello_world():
    return "<p> Hello, World! </p>"

@home.route('/flights', methods = ['GET', 'POST'])
def search_flight():
    if request.method == 'POST':
        airline_name = request.form['AirlineName']
        flight_number = request.form['FlightNumber']
        date = request.form['Date']
        choice = request.form['dateChoice']

        cursor = conn.cursor()
        if choice == 'ARRIVAL':
            cursor.execute(search_status_arrival_query, (airline_name, flight_number, date))
        else:
            cursor.execute(search_status_departure_query, (airline_name, flight_number, date))
        return render_template('checking_flight_status.html')
            
        
    return render_template('checking_flight_status.html')

@home.route('/flights/status')
def get_status_result():
    return "<p> Hello, World! </p>"
