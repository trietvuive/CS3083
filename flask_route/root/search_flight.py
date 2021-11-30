from flask import Blueprint, render_template, request, redirect, url_for
from route import flights
from settings import *
import pymysql

@flights.route('/search', methods = ['GET', 'POST'])
def search_flight():
    if request.method == 'POST':
        destination = request.form['To']
        source = request.form['From']

        depart_date = request.form['departure']
        return_date = request.form['return']
        # either oneway or round
        trip = request.form['trip']

        cursor = conn.cursor()
        if trip == 'oneway':
            cursor.execute(search_oneway_airport_query, (depart_date, source, destination))
            
        else:
            cursor.execute(search_twoway_airport_query, (depart_date, return_date, source, destination))
        records = cursor.fetchall()
        # Wait for a table template to display all the records...
        return redirect(url_for('customer.home', name = depart_date))
        
    return render_template('flight/search_flights.html')

