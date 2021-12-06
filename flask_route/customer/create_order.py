from flask import render_template, redirect, url_for, Blueprint, request, session
import pymysql
import hashlib
from settings import *
from route import customer

# Add a new route /customer/register to cust_auth blueprint
@customer.route('/create_order/', methods = ['GET','POST'])
def create_order():
    status = ''
    if 'customer_email' not in session:
        return redirect(url_for('customer.login'))

    flight_number = request.args['flight_number']
    airline = request.args['airline']
    depart_date = request.args['depart_date']
    email = session['customer_email']
    print(flight_number, airline, depart_date)

    cursor = conn.cursor()
    cursor.execute(number_of_seats, (airline, flight_number, depart_date))
    seat_count = cursor.fetchone()['num_seats']

    cursor.execute(base_price, (airline, flight_number, depart_date))
    price_based = cursor.fetchone()['base_price']

    cursor.execute(tickets_sold, (airline, flight_number, depart_date))
    sold_tickets = cursor.fetchone()['ticket']

    print(seat_count, price_based, sold_tickets)

    true_price = getSoldPrice(int(sold_tickets), int(seat_count), int(price_based))
    
    if request.method == 'POST':
        post_tuple = create_POST_tuple(['paymentMethod', 'cardNumber', 'cardholderName', 'cardDate', 'cvv'],request.form)
        print(post_tuple)
        cursor.execute(ticket_id)
        unique_ticket = cursor.fetchone()['id']
        try:
            # Insert a record into Ticket table
            cursor.execute(cust_purchase_ticket, (unique_ticket, true_price, airline, flight_number, depart_date,
                                              post_tuple[0], post_tuple[1], post_tuple[2], post_tuple[3]))

            # Insert a record to Purchase table
            cursor.execute(cust_record_purchase, (email, unique_ticket))

            # Insert a record into Takes table
            cursor.execute(cust_ins_takes, (email, airline, flight_number, depart_date))

            status = "Purchase successful!"
            
        except Exception as e:
            print(e)
            status = "Error..."
    cursor.close()
    
    return render_template('customer/payment.html', description = flight_number, price = str(true_price), status = status)
