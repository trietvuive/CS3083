from flask import render_template, Blueprint, request, session, redirect, url_for
from route import staff
from settings import development

@staff.route('/')
def home():
    if 'staff_username' not in session:
        return redirect(url_for('staff.login'))
    return render_template('staff/staff_home.html', email = session['staff_username'])

@staff.route('/logout')
def logout():
    session.pop('staff_username', None)
    session.pop('staff_airline', None)
    return redirect(url_for('staff.login'))
