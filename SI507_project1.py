# Import statements necessary
from flask import Flask
from lab3_code import *

# Set up application
app = Flask(__name__)

# Routes
@app.route('/')
def basic():
    return 'Welcome to the banking app!'



@app.route('/bank/<name>')
def welcome_name(name):
    bank_name = Bank(name)
    return "Welcome to {}!".format(bank_name)

# Something else to note is that the functions don't get INVOKED the way you may be used to. Running the application and *going to a URL that matches the path in the @app.route() business IS what runs that function!


@app.route('/showvalues/<name>/<greeting>')
def showvalues(name, greeting): # Check this out -- what's going on here? A useful pattern to think about.
    return "{}, {}!".format(greeting, name)
