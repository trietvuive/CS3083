import pymysql
import hashlib

# store global variables, basically 

cust_log_veri_query = 'SELECT * FROM Customer WHERE email = %s AND pwd = %s'
cust_reg_veri_query = 'SELECT * FROM Customer WHERE email = %s'
cust_ins_query = 'INSERT INTO Customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'trietrie',
                       db='CS3083',
                       charset = 'utf8mb4',
                       cursorclass = pymysql.cursors.DictCursor)

def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

