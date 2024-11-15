from flask import Flask, request, render_template, jsonify
from main_logic import *
from app.random_contents import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)