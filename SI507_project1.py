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
    bank_insts = Bank(name, Dollar, 1)
    bank_name = bank_insts.name
    return 'Welcome to {}!'.format(bank_name)


@app.route('/dollar/<amt>')
def dollar_app(amt):
    num = int(amt)
    num_insts = Dollar(num)
    return num_insts.__str__()


@app.route('/yuan/<amt>')
def yuan_app(amt):
    num = int(amt)
    num_insts = Yuan(num)
    return num_insts.__str__()


@app.route('/pound/<amt>')
def pound_app(amt):
    num = int(amt)
    num_insts = Pound(num)
    return num_insts.__str__()


@app.route('/bank/<name>/<currency>/<value>')
def final(name,currency,value):
    new_currency = currency.lower()
    if new_currency == 'dollar':
        num = int(value)
        num_insts = Dollar(num)
        return 'Welcome to the {} bank! {} Bank holds the {} currency and currently holds {}.'.format(name,name, new_currency, num_insts.__str__())

    if new_currency == 'yuan':
        num = int(value)
        num_insts = Yuan(num)
        return 'Welcome to the {} bank! {} Bank holds the {} currency and currently holds {}.'.format(name,name, new_currency, num_insts.__str__())

    if new_currency == 'pound':
        num = int(value)
        num_insts = Pound(num)
        return 'Welcome to the {} bank! {} Bank holds the {} currency and currently holds {}.'.format(name,name, new_currency, num_insts.__str__())

    else:
        return 'Invalid URL inputs for bank.'


if __name__ == "__main__":
    app.run()
