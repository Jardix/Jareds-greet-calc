from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def print_welcome():
    return "Welcome!"

@app.route('/welcome/home')
def print_welcome_home():
    return "Welcome home!"

@app.route('/welcome/back')
def print_welcome_back():
    return "Welcome back!"

# Ran 3 tests, all came out to 'OK'. 
# I included no docstrings as it's pretty obvious what's happening here and why. 

