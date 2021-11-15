from flask import Flask, render_template, session, redirect, url_for, request, escape
import pymysql
import hashlib

app = Flask("Triet")
"""
conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = 'trietrie',
                       db='CS3083',
                       charset = 'utf8mb4',
                       cursorclass = pymysql.cursors.DictCursor)


def md5(s):
    return hashlib.md5(s).hexdigest()
"""
@app.route("/")
def hello_world():
    return "<p> Hello, World! </p>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name = name)

@app.route('/login/', methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        """
        username = escape(request.form['username'])
        password = md5(escape(request.form['password']))
        cursor = conn.cursor()
        query = 'SELECT * FROM user WHERE username = %s AND password = %s'
        cursor.execute(query, (username, password))

        data = cursor.fetchone()
        cursor.close()
        """
        # if not (request.form['username'] == 'admin' and request.form['password'] == 'admin') and not data:
        if not (request.form['username'] == 'admin' and request.form['password'] == 'admin'):
            error = 'Invalid Credentials...'
        else:
            return redirect(url_for('hello'))
    return render_template('login.html', error = error)

"""
@app.route('/register/', methods = ['GET','POST'])
def register():
    error = None
    if request.method == 'POST':
        
        username = request.form['username']
        password = md5(escape(request.form['password']))
        cursor = conn.cursor()
        query = 'SELECT * FROM user WHERE username = %s'
        cursor.execute(query, (username))

        data = cursor.fetchone()

        if data:
            error = 'This user already exists'
        else:
            ins = 'INSERT INTO user VALUES(%s, %s)'
            cursor.execute(ins, (username, password))
            conn.commit()
            error = 'Registered =)'
        cursor.close()
    return render_template('login.html', error = error)
"""
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)

