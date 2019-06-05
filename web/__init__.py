from flask import Flask, render_template, session, redirect, url_for, escape, request
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'iunew842o3vu8n'


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect(url_for("login"))


@app.route("/login", methods=['GET', 'POST'])
def login(invalid=False):
    if request.method == 'POST':
        if request.form['username'] == 'admin' and \
                request.form['password'] == 'bongo':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            return render_template("login.html", invalid=True)
    return render_template("login.html")


@app.route("/")
def index():
    if 'username' in session:
        return render_template("index.html")
    return redirect(url_for('login'))


@app.route("/analytics")
def analytics():
    if 'username' in session:
        return render_template("analytics.html")
    return redirect(url_for('login'))


@app.route("/books")
def books(error=None):
    if 'username' in session:
        return render_template("books.html")
    return redirect(url_for('login'))


@app.route("/book", methods=['GET', 'POST'])
def book():
    if 'username' in session:
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
    return redirect(url_for('login'))


def start():
    app.debug = True
    # app.use_reloader = False
    app.run(debug=True, threaded=True)
