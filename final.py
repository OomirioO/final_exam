from flask import Flask, request
from flask import render_template
import random

app = Flask(__name__)

sum_result=0

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/random")
def rand():
    global ran
    ran=random.random()
    return ran

@app.route("/sum")
def sum():
    sum_result=ran+sum_result
    return sum_result

if __name__ == "__main__":
    app.run(host="0.0.0.0")