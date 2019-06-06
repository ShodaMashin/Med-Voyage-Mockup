from flask import Flask, render_template, session, redirect, url_for, escape, request
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'iunew842o3vu8n'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/providers")
def providers():
    return render_template("providers.html")


@app.route("/comparison")
def comparison():
    return render_template("comparison.html")


@app.route("/consultation")
def consultation():
    return render_template("consultation.html")


@app.route("/flights")
def flights():
    return render_template("flights.html")


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


def start():
    app.debug = True
    # app.use_reloader = False
    app.run(debug=True, threaded=True)
