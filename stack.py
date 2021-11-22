from flask import Flask, render_template, session, redirect, url_for, request, escape
import pymysql
import hashlib

app = Flask("Triet")

conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'trietrie',
                       db='CS3083',
                       charset = 'utf8mb4',
                       cursorclass = pymysql.cursors.DictCursor)


def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

@app.route("/")
def hello_world():
    return "<p> Hello, World! </p>"

@app.route('/hello/')
def hello():
    return render_template('hello.html', name = request.args.get('name'))

@app.route('/login/', methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        print(username)
        password = md5(request.form['password'])
        cursor = conn.cursor()
        query = 'SELECT * FROM Users WHERE username = %s AND password = %s'
        cursor.execute(query, (username, password))

        data = cursor.fetchone()
        cursor.close()
        if not (request.form['username'] == 'admin' and request.form['password'] == 'admin') and not data:
            error = 'Invalid Credentials...'
        else:
            return redirect(url_for('hello', name = username))
    return render_template('login.html', error = error)

@app.route('/register/', methods = ['GET','POST'])
def register():
    status = None
    if request.method == 'POST':
        
        username = request.form['username']
        password = md5(escape(request.form['password']))
        cursor = conn.cursor()
        query = 'SELECT * FROM Users WHERE username = %s'
        cursor.execute(query, (username))

        data = cursor.fetchone()

        if data:
            status = 'This user already exists'
        else:
            ins = 'INSERT INTO Users VALUES(%s, %s)'
            cursor.execute(ins, (username, password))
            conn.commit()
            status = 'Registered =)'
        cursor.close()
    return render_template('register.html', status = status)
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)

