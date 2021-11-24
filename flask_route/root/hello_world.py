from flask import Blueprint
from route import home

@home.route("/")
def hello_world():
    return "<p> Hello, World! </p>"
