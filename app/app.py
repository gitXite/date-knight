from flask import Flask, request, render_template, jsonify
from main_logic import get_random_activities, get_city, get_activities_by_category, get_number_activities
from random_contents import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generator')
def generator():
    return render_template('generator.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True)
