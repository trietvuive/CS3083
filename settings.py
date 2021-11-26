import pymysql
import hashlib

# store global variables, basically 

cust_log_veri_query = 'SELECT * FROM Customer WHERE email = %s AND pwd = %s'
cust_reg_veri_query = 'SELECT * FROM Customer WHERE email = %s'
cust_ins_query = 'INSERT INTO Customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

staff_log_veri_query = 'SELECT * FROM AirlineStaff WHERE username = %s AND password = %s'
staff_reg_veri_query = 'SELECT * FROM AirlineStaff WHERE username = %s'
staff_ins_query = 'INSERT INTO AirlineStaff VALUES(%s, %s, %s, %s, %s, %s)'
staff_ins_phone_query = 'INSERT INTO StaffPhoneNumbers VALUES(%s, %s)'

search_oneway_airport_query = 'SELECT * ' \
                              'FROM flight ' \
                              'WHERE depart_datetime > CURRENT_TIMESTAMP ' \
                              'AND depart_datetime = %s ' \
                              'AND depart_airport = %s ' \
                              'AND arrival_airport IN ' \
                              '(SELECT code FROM airport WHERE name = %s)'
search_oneway_city_query = 'SELECT * ' \
                           'FROM flight ' \
                           'WHERE depart_datetime > CURRENT_TIMESTAMP ' \
                           'AND depart_datetime = %s ' \
                           'AND depart_airport IN ' \
                           '(SELECT code ' \
                           'FROM airport ' \
                           'WHERE city = %s) ' \
                           'AND arrival_airport IN ' \
                           '(SELECT code FROM airport WHERE city = %s)'
search_twoway_airport_query = 'SELECT * ' \
                              'FROM flight AS dep, flight AS ret ' \
                              'WHERE dep.depart_datetime > CURRENT_TIMESTAMP ' \
                              'AND dep.flight_num = ret.flight_num ' \
                              'AND dep.depart_datetime < ret.depart_datetime ' \
                              'AND dep.depart_datetime = %s ' \
                              'AND ret.depart_datetime = %s ' \
                              'AND dep.depart_airport IN ' \
                              '(SELECT code FROM airport WHERE name = %s) ' \
                              'AND dep.arrival_airport IN ' \
                              '(SELECT code FROM airport WHERE name = %s) '
search_twoway_city_query =  'SELECT *' \
                            'FROM flight AS dep, flight AS ret ' \
                            'WHERE dep.depart_datetime > CURRENT_TIMESTAMP ' \
                            'AND dep.flight_num = ret.flight_num ' \
                            'AND dep.depart_datetime < ret.depart_datetime ' \
                            'AND dep.depart_datetime = %s ' \
                            'AND ret.depart_datetime = %s ' \
                            'AND dep.depart_airport IN ' \
                            '(SELECT code FROM airport WHERE city = %s) ' \
                            'AND dep.arrival_airport IN ' \
                            '(SELECT code FROM airport WHERE city = %s)'

search_status_departure_query = 'SELECT airline_name, flight_num, depart_datetime AS date, status FROM Flight WHERE airline_name = %s AND flight_num = %s AND depart_datetime = %s'
search_status_arrival_query =   'SELECT airline_name, flight_num, arrival_datetime AS date, status FROM Flight WHERE airline_name = %s AND flight_num = %s AND arrival_datetime = %s'

conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'trietrie',
                       db='CS3083',
                       charset = 'utf8mb4',
                       cursorclass = pymysql.cursors.DictCursor)

def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

