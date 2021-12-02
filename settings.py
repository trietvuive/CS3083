import pymysql
import hashlib

# development mode
development = True

# store global variables, basically 

conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'trietrie',
                       db='CS_3083',
                       charset = 'utf8mb4',
                       cursorclass = pymysql.cursors.DictCursor)

# ------------------------------------ General Use Cases --------------------------------------------

# Use Case 1
# Searching for Oneway Flights by Airport Name
search_oneway_airport_query ='SELECT * ' \
                             'FROM Flight ' \
                             'WHERE depart_datetime > CURRENT_TIMESTAMP ' \
                             'AND CAST(depart_datetime AS date) = %s ' \
                             'AND depart_airport = %s ' \
                             'AND arrival_airport = %s'

# Searching for Oneway Flights by City Name
search_oneway_city_query = 'SELECT * ' \
                           'FROM Flight ' \
                           'WHERE depart_datetime > CURRENT_TIMESTAMP ' \
                           'AND CAST(depart_datetime AS date) = %s' \
                           'AND depart_airport IN ' \
                           '(SELECT code FROM Airport WHERE city = %s) ' \
                           'AND arrival_airport IN ' \
                           '(SELECT code FROM Airport WHERE city = %s)'

# Searching for Twoway Flights by Airport Name
search_twoway_airport_query = 'SELECT * ' \
                              'FROM Flight AS dep, Flight AS ret ' \
                              'WHERE dep.depart_datetime > CURRENT_TIMESTAMP ' \
                              'AND dep.depart_datetime < ret.depart_datetime ' \
                              'AND dep.airline_name = ret.airline_name ' \
                              'AND CAST(dep.depart_datetime AS date) = %s ' \
                              'AND CAST(ret.depart_datetime AS date) = %s ' \
                              'AND dep.depart_airport IN ' \
                              '(SELECT code FROM Airport WHERE name = %s) ' \
                              'AND dep.arrival_airport IN ' \
                              '(SELECT code FROM Airport WHERE name = %s)'

# Searching for Twoway Flights by City Name
search_twoway_city_query = 'SELECT * ' \
                           'FROM Flight AS dep, Flight AS ret ' \
                           'WHERE dep.depart_datetime > CURRENT_TIMESTAMP ' \
                           'AND dep.depart_datetime < ret.depart_datetime ' \
                           'AND dep.airline_name = ret.airline_name ' \
                           'AND CAST(dep.depart_datetime AS date) = %s ' \
                           'AND CAST(ret.depart_datetime AS date) = %s ' \
                           'AND dep.depart_airport IN ' \
                           '(SELECT code FROM Airport WHERE city = %s) ' \
                           'AND dep.arrival_airport IN ' \
                           '(SELECT code FROM Airport WHERE city = %s) '

# Searching for Flight Status by Departure Date
search_status_departure_query = 'SELECT airline_name, flight_num, CAST(depart_datetime AS date) AS date, status FROM Flight WHERE airline_name = %s AND flight_num = %s AND CAST(depart_datetime AS date) = %s'

# Searching for Flight Status by Arrival Date
search_status_arrival_query =   'SELECT airline_name, flight_num, CAST(arrival_datetime AS date) AS date, status FROM Flight WHERE airline_name = %s AND flight_num = %s AND CAST(arrival_datetime AS date) = %s'

# Use Case 2
# Customer Register & Verification
# email, pwd, name, add_building_num, add_street, add_city,
# add_state, phone_number, passport_num, passport_expiration,
# passport_country, date_of_birth
cust_ins_query = 'INSERT INTO Customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
cust_reg_veri_query = 'SELECT * FROM Customer WHERE email = %s'

# Staff Register & Verification
# username, password, airline, first_name, last_name, date_of_birth
staff_ins_query = 'INSERT INTO AirlineStaff VALUES(%s, %s, %s, %s, %s, %s)'
staff_ins_phone_query = 'INSERT INTO StaffPhoneNumbers VALUES(%s, %s)'
staff_reg_veri_query = 'SELECT * FROM AirlineStaff WHERE username = %s'

# Use Case 3
# Customer Login
cust_log_veri_query = 'SELECT * FROM Customer WHERE email = %s AND password = %s'

# Staff Login
staff_log_veri_query = 'SELECT * FROM AirlineStaff WHERE username = %s AND password = %s'

# -------------------------------------------- Customer Use Cases --------------------------------------------

# Use Case 4
# View MY Flights
# View All Future Flights
cust_future_flights = 'SELECT * ' \
                      'FROM Flight ' \
                      'WHERE (airline_name, flight_num) IN ' \
                      '(SELECT airline, flight_num ' \
                      'FROM Ticket, Purchases ' \
                      'WHERE id = t_id AND cust_email = %s ' \
                      'AND depart_datetime > CURRENT_TIMESTAMP)'

# View All Flights in a Range of Dates
cust_range_flights = 'SELECT * ' \
                     'FROM Flight ' \
                     'WHERE (airline_name, flight_num) IN ' \
                     '(SELECT airline, flight_num ' \
                     'FROM Ticket, Purchases ' \
                     'WHERE id = t_id AND cust_email = %s ' \
                     'AND CAST(depart_datetime AS date) >= %s ' \
                     'AND CAST(depart_datetime AS date) <= %s)'

# Use Case 5
# Use searches from general use cases

# Use Case 6 -- NOT FINISHED OR TESTED
# Buy a Ticket
# Figure out sold price
number_of_seats = 'SELECT num_seats ' \
                  'FROM Airplane ' \
                  'WHERE (airline, id) IN ' \
                  '(SELECT airplane_id, airplane_airline_name ' \
                  'FROM Flight ' \
                  'WHERE airline_name = %s AND flight_num = %s AND depart_datetime = %s)'

base_price = 'SELECT base_price FROM Flight WHERE airline_name = %s AND flight_num = %s AND depart_datetime = %s'

tickets_sold = 'SELECT COUNT(id) FROM Ticket WHERE airline = %s AND flight_num = %s AND depart_datetime = %s'

def getSoldPrice(ticketsSold, numberOfSeats, basePrice):
    if ticketsSold >= numberOfSeats * 0.75:
        return basePrice + (basePrice * 1.25)
    else:
        return basePrice

# Unique ID
ticket_id = 'SELECT UUID_TO_BIN(UUID())'

# Purchase the Ticket
# id, sold_price, airline, flight_num, depart_datetime, pay_card_type, pay_card_num, pay_name_on_card, pay_card_expiration
cust_purchase_ticket = 'INSERT INTO Ticket VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'

# Record Purchase (Need to have same ticket id as UUID())
# cust_email, t_id
cust_record_purchase = 'INSERT INTO Purchases VALUES(%s, %s, CURRENT_TIMESTAMP)'

# Use Case 7
# Add Rating and Comment to a Previous Flight
# Info needs to be added to Takes at some point
# No comment or rating initially
# cust_email, flight_airline, flight_num, flight_depart_datetime
cust_ins_takes = 'INSERT INTO Takes VALUES(%s, %s, %s, %s, NULL, NULL)'

cust_rate_comment = 'UPDATE Takes ' \
                    'SET comment = %s, rating = %i ' \
                    'WHERE cust_email = %s AND flight_airline = %s ' \
                    'AND flight_num = %s AND flight_depart_datetime = %s'

# Use Case 8
# Total Spent in Past Year
cust_spent_year = 'SELECT SUM(sold_price) ' \
                  'FROM Purchases, Ticket ' \
                  'WHERE cust_email = %s AND t_ID = ID ' \
                  'AND CAST(date_time AS date) >= DATE_ADD(CURDATE(), INTERVAL -1 YEAR) ' \
                  'AND CAST(date_time AS date) <= CURDATE()'

# Total Spent in Last 6 Months by Month (DEFAULT)
cust_spent_monthly_sixmonths = 'SELECT YEAR(date_time), MONTHNAME(date_time), SUM(sold_price) ' \
                     'FROM Purchases, Ticket ' \
                     'WHERE cust_email = %s AND t_ID = ID ' \
                     'AND CAST(date_time AS date) >= DATE_ADD(CURDATE(), INTERVAL -6 MONTH) ' \
                     'AND CAST(date_time AS date) <= CURDATE() ' \
                     'GROUP BY YEAR(date_time), MONTHNAME(date_time) ' \
                     'ORDER BY YEAR(date_time), MONTHNAME(date_time)'

# Total Spent in Range of Dates by Month
cust_spent_monthly_range = 'SELECT YEAR(date_time), MONTHNAME(date_time), SUM(sold_price) ' \
                           'FROM Purchases, Ticket ' \
                           'WHERE cust_email = %s AND t_ID = ID ' \
                           'AND CAST(date_time AS date) >= %s ' \
                           'AND CAST(date_time AS date) <= %s ' \
                           'GROUP BY YEAR(date_time), MONTHNAME(date_time) ' \
                           'ORDER BY YEAR(date_time), MONTHNAME(date_time)'

# -------------------------------------------- Staff Use Cases -----------------------------------------------
# NO USE CASES TESTED

# Use Case 4
# Show All Future Flights Operated by Staff's Airline in Next 30 Days (DEFAULT)
staff_show_flights_30days = 'SELECT * FROM Flight ' \
                            'WHERE CAST(depart_datetime AS date) >= CURDATE() ' \
                            'AND CAST(depart_datetime AS date) <= DATE_ADD(CURDATE(), INTERVAL 30 DAY) ' \
                            'AND airline_name IN ' \
                            '(SELECT airline ' \
                            'FROM AirlineStaff ' \
                            'WHERE username = %s)'

# Show All Flights Operated by Staff's Airline in Range of Dates
staff_show_flights_range = 'SELECT * ' \
                           'FROM Flight ' \
                           'WHERE CAST(depart_datetime AS date) >= %s ' \
                           'AND CAST(depart_datetime AS date) <= %s ' \
                           'AND airline_name IN ' \
                           '(SELECT airline ' \
                           'FROM AirlineStaff ' \
                           'WHERE username = %s)'

# Show All Customers of a Flight
staff_show_customers = 'SELECT email, name ' \
                       'FROM Customer, Purchases ' \
                       'WHERE email = cust_email AND t_id IN ' \
                       '(SELECT id ' \
                       'FROM Ticket ' \
                       'WHERE airline = %s AND flight_num = %s AND depart_datetime = %s)'

# Use Case 5
# Add a New Flight
# airline_name, flight_num, depart_datetime, depart_airport,
# arrival_datetime, arrival_airport, base_price, airplane_id,
# airplane_airline_name, status
staff_ins_flight = 'INSERT INTO Flight VALUES(%s, %s, %s, %s, %s, %s, %d, %s, %s, %s)'

# Show Flights Operated by Staff's Airline for Next 30 Days (Confirmation Page)
# Use staff_show_flights_30days

# Use Case 6
# Update Flight Status
staff_upd_status = 'UPDATE Flight SET status = %s WHERE airline_name = %s AND flight_num = %s AND depart_datetime = %s'

# Use Case 7
# Add Airplane
# airline, id, num_seats
staff_ins_airplane = 'INSERT INTO Airplane (airline, ID, num_seats) VALUES(%s, %s, %s)'

# Show All Airplanes Owned by Staff's Airline (Confirmation Page)
staff_show_airplanes = 'SELECT id, num_seats FROM Airplane NATURAL JOIN AirlineStaff WHERE username = %s'

# Use Case 8
# Add Airport
# code, name, city
staff_ins_airport = 'INSERT INTO Airport (city, code, name) VALUES(%s, %s, %s)'

# Use Case 9
# Average Rating for a Flight
staff_show_avg_rating = 'SELECT flight_airline, flight_num, flight_depart_datetime, AVG(rating) AS Average Rating ' \
                        'FROM Takes ' \
                        'WHERE flight_airline = %s AND flight_num = %s ' \
                        'AND flight_depart_datetime = %s ' \
                        'GROUP BY flight_airline, flight_num, flight_depart_datetime'

# Ratings and Comments for a Flight
staff_show_ratings_comments = 'SELECT cust_email, comment, rating ' \
                              'FROM Takes ' \
                              'WHERE flight_airline IN ' \
                              '(SELECT airline ' \
                              'FROM AirlineStaff ' \
                              'WHERE username = %s) ' \
                              'AND flight_num = %s ' \
                              'AND flight_depart_datetime = %s'

# Use Case 10
# View Most Frequent Customer Within Last Year
staff_show_freq_customer = 'SELECT cust_email, COUNT(cust_email) ' \
                           'FROM Takes ' \
                           'WHERE flight_airline IN ' \
                           '(SELECT airline ' \
                           'FROM AirlineStaff ' \
                           'WHERE username = %s) ' \
                           'AND CAST(flight_depart_datetime AS date) >= DATE_ADD(CURDATE(), INTERVAL -1 YEAR) ' \
                           'AND CAST(flight_depart_datetime AS date) <= CURDATE() ' \
                           'AND cust_email NOT IN ' \
                           '(SELECT s.cust_email ' \
                           'FROM Takes AS s, TAKES AS t ' \
                           'WHERE COUNT(s.cust_email) < COUNT(t.cust_email))'

# View All Flights a Customer Has Taken on Airline
staff_show_customer_flights = 'SELECT flight_num, flight_depart_datetime ' \
                              'FROM Takes ' \
                              'WHERE cust_email = %s ' \
                              'AND flight_airline IN ' \
                              '(SELECT airline ' \
                              'FROM AirlineStaff ' \
                              'WHERE username = %s)'

# Use Case 11
# View Reports
# Total Amount of Tickets Sold in Range of Dates
staff_total_tickets_sold = 'SELECT COUNT(t_id) ' \
                           'FROM Ticket, Purchases ' \
                           'WHERE id = t_id ' \
                           'AND CAST(date_time AS date) >= %s ' \
                           'AND CAST(date_time AS date) <= %s ' \
                           'AND airline IN ' \
                           '(SELECT airline ' \
                           'FROM AirlineStaff ' \
                           'WHERE username = %s)'

# Monthwise Tickets Sold in Range of Dates
staff_monthwise_tickets_sold = 'SELECT YEAR(date_time), MONTHNAME(date_time), COUNT(t_id) ' \
                               'FROM Ticket, Purchases ' \
                               'WHERE id = t_id ' \
                               'AND CAST(date_time AS date) >= %s ' \
                               'AND CAST(date_time AS date) <= %s ' \
                               'AND airline IN ' \
                               '(SELECT airline ' \
                               'FROM AirlineStaff ' \
                               'WHERE username = %s) ' \
                               'GROUP BY YEAR(date_time), MONTHNAME(date_time) ' \
                               'ORDER BY YEAR(date_time), MONTHNAME(date_time)'

# Use Case 12
# View Earnings
# Revenue of Ticket Sales in Last Month
staff_revenue_month = 'SELECT SUM(sold_price) ' \
                      'FROM Ticket, Purchases ' \
                      'WHERE t_id = id ' \
                      'AND CAST(date_time AS date) >= DATE_ADD(CURDATE(), INTERVAL -1 MONTH) ' \
                      'AND CAST(date_time AS date) <= CURDATE() ' \
                      'AND airline IN ' \
                      '(SELECT airline ' \
                      'FROM AirlineStaff ' \
                      'WHERE username = %s)'

# Revenue of Ticket Sales in Last Year
staff_revenue_year = 'SELECT SUM(sold_price) ' \
                     'FROM Ticket, Purchases ' \
                     'WHERE t_id = id ' \
                     'AND CAST(date_time AS date) >= DATE_ADD(CURDATE(), INTERVAL -1 YEAR) ' \
                     'AND CAST(date_time AS date) <= CURDATE() ' \
                     'AND airline IN ' \
                     '(SELECT airline ' \
                     'FROM AirlineStaff ' \
                     'WHERE username = %s)'

# Use Case 13 -- NOT FINISHED
# Top 3 Destinations in Last 3 Months
staff_top_destinations_month = 'SELECT city ' \
                               'FROM Airport ' \
                               'WHERE code IN ' \
                               '(SELECT DISTINCT arrival_airport ' \
                               'FROM Flight NATURAL JOIN Ticket ' \
                               'WHERE airline_name = airline ' \
                               'AND CAST(depart_datetime AS date) >= DATE_ADD(CURDATE(), INTERVAL -3 MONTH) ' \
                               'AND CAST(depart_dateime AS date) <= CURDATE() ' \
                               'GROUP BY arrival_airport ' \
                                'HAVING COUNT(id) = MAX(COUNT(id)))'

# Top 3 Destinations in Last Year
staff_top_destinations_year = 'SELECT city ' \
                              'FROM Airport ' \
                              'WHERE code IN ' \
                              '(SELECT DISTINCT arrival_airport ' \
                              'FROM Flight NATURAL JOIN Ticket ' \
                              'WHERE airline_name = airline ' \
                              'AND CAST(depart_datetime AS date) >= DATE_ADD(CURDATE(), INTERVAL -1 YEAR) ' \
                              'AND CAST(depart_dateime AS date) <= CURDATE() ' \
                              'GROUP BY arrival_airport ' \
                              'HAVING COUNT(id) = MAX(COUNT(id)))'

def md5(s):
    return hashlib.md5(s.encode()).hexdigest()
def create_POST_tuple(parameter_list, form):
    return tuple((form[i] for i in parameter_list))

