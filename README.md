# CS3083
CS3083 Project. Hosted on stack.trietmvo.com!

# How to run?
source the virtualenv. </br>
For windows, ./venv/bin/activate and $env:FLASK_APP = 'stack', then flask run </br>
For linux, export FLASK_APP=stack, then flask run
If none of these works, just pip install -r requirements.txt and python stack.py

# Overview: </br>
flask_route contains all the possible route that the web application can go to. </br>
sql contains all the create table and insert data query we used to populate the database. </br>
server_config is all the file we used to setup nginx and wsgi in the public server. </br>
static contains all the css, js and images we used to design the frontend. </br>
venv, env and window_env are Python virtual environments that we used to setup the Linux server and develop on Window. </br>
templates contains all the html files. it's quite messy right now. </br>
stack.ini is used for setting up wsgi. </br>
route.py setup all the Flask Blueprint that contains the major route we used. </br>
stack.py is the entrypoint to the application. </br>
wsgi.py is the entrypoint for wsgi. </br>

