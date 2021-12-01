import pymysql
import hashlib

# development mode
development = True

# store global variables, basically 

cust_log_veri_query = 'SELECT * FROM Customer WHERE email = %s AND pwd = %s'
cust_reg_veri_query = 'SELECT * FROM Customer WHERE email = %s'
cust_ins_query = 'INSERT INTO Customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

staff_log_veri_query = 'SELECT * FROM AirlineStaff WHERE username = %s AND password = %s'
staff_reg_veri_query = 'SELECT * FROM AirlineStaff WHERE username = %s'
staff_ins_query = 'INSERT INTO AirlineStaff VALUES(%s, %s, %s, %s, %s, %s)'
staff_ins_phone_query = 'INSERT INTO StaffPhoneNumbers VALUES(%s, %s)'

# Searching for Oneway Flights by Airport Name
search_oneway_airport_query ='SELECT *' \
                             'FROM Flight' \
                             'WHERE depart_datetime > CURRENT_TIMESTAMP' \
                             'AND CAST(depart_datetime AS date) = %s' \
                             'AND depart_airport IN' \
                             '(SELECT code FROM Airport WHERE name = %s)' \
                             'AND arrival_airport IN' \
                             '(SELECT code FROM Airport WHERE name = %s)'

# Searching for Oneway Flights by City Name
search_oneway_city_query = 'SELECT *' \
                           'FROM Flight' \
                           'WHERE depart_datetime > CURRENT_TIMESTAMP ' \
                           'AND CAST(depart_datetime AS date) = %s' \
                           'AND depart_airport IN ' \
                           '(SELECT code FROM Airport WHERE city = %s)' \
                           'AND arrival_airport IN' \
                           '(SELECT code FROM Airport WHERE city = %s)'

# Searching for Twoway Flights by Airport Name
search_twoway_airport_query = 'SELECT *' \
                              'FROM Flight AS dep, Flight AS ret' \
                              'WHERE dep.depart_datetime > CURRENT_TIMESTAMP' \
                              'AND dep.depart_datetime < ret.depart_datetime' \
                              'AND dep.airline_name = ret.airline_name' \
                              'AND CAST(dep.depart_datetime AS date) = %s' \
                              'AND CAST(ret.depart_datetime AS date) = %s' \
                              'AND dep.depart_airport IN' \
                              '(SELECT code FROM Airport WHERE name = %s)' \
                              'AND dep.arrival_airport IN' \
                              '(SELECT code FROM Airport WHERE name = %s)'

# Searching for Twoway Flights by City Name
search_twoway_city_query = 'SELECT *' \
                           'FROM Flight AS dep, Flight AS ret' \
                           'WHERE dep.depart_datetime > CURRENT_TIMESTAMP ' \
                           'AND dep.depart_datetime < ret.depart_datetime' \
                           'AND dep.airline_name = ret.airline_name' \
                           'AND CAST(dep.depart_datetime AS date) = %s' \
                           'AND CAST(ret.depart_datetime AS date) = %s' \
                           'AND dep.depart_airport IN' \
                           '(SELECT code FROM Airport WHERE city = %s)' \
                           'AND dep.arrival_airport IN' \
                           '(SELECT code FROM Airport WHERE city = %s)'

# Searching for Flight Status by Departure Date
search_status_departure_query = 'SELECT airline_name, flight_num, CAST(depart_datetime AS date) AS date, status FROM Flight WHERE airline_name = %s AND flight_num = %s AND CAST(depart_datetime AS date) = %s'

# Searching for Flight Status by Arrival Date
search_status_arrival_query =   'SELECT airline_name, flight_num, CAST(arrival_datetime AS date) AS date, status FROM Flight WHERE airline_name = %s AND flight_num = %s AND CAST(arrival_datetime AS date) = %s'

conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'trietrie',
                       db='CS3083',
                       charset = 'utf8mb4',
                       cursorclass = pymysql.cursors.DictCursor)

def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

