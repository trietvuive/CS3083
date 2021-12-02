from flask import Blueprint, render_template, request, redirect, url_for
from route import flights
from settings import *
import pymysql

@flights.route('/search', methods = ['GET', 'POST'])
def search_flight():
    flights = None
    if request.method == 'POST':
        destination = request.form['To']
        source = request.form['From']

        depart_date = request.form['departure']
        return_date = request.form['return']
        trip = request.form['trip']

        print(destination, source, depart_date, return_date, trip)
        cursor = conn.cursor()
        if trip == 'one-way':
            cursor.execute(search_oneway_airport_query, (depart_date, source, destination))
            
        else:
            cursor.execute(search_twoway_airport_query, (depart_date, return_date, source, destination))
        records = cursor.fetchall()
        cursor.close()
        return render_template('flight/flights_table.html', flights = records)
    return render_template('flight/search_flights.html')

