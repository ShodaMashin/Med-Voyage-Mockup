from flask import Flask, render_template, session, redirect, url_for, escape, request
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'iunew842o3vu8n'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analytics")
def analytics():
    return render_template("analytics.html")


@app.route("/books")
def books(error=None):
    return render_template("books.html")


@app.route("/book", methods=['GET', 'POST'])
def book():
    error = None
    if request.method == 'POST':
        error = False
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        try:
            published = datetime.strptime(request.form["published"], '%Y-%m-%d')
        except ValueError:
            error = True
        if error == False:
            return render_template("books.html", error=error)
    return render_template("addBook.html", error=error)


def start():
    app.debug = True
    # app.use_reloader = False
    app.run(debug=True, threaded=True)
