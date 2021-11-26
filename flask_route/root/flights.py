from flask import Blueprint, render_template, request
from route import flights
from settings import *
import pymysql

@flights.route('/', methods = ['GET', 'POST'])
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
        records = cursor.fetchall()

        return render_template('flight/bootstrap_table.html', title = 'Status', flights = records, departure = choice == 'DEPARTURE')
            
        
    return render_template('flight/checking_flight_status.html')

