import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    rows = db.execute("SELECT symbol, shares, price FROM purchases")
    cash = db.execute("SELECT cash FROM users")
    total = db.execute("SELECT SUM(shares * price) AS total_value FROM purchases")
    return render_template("index.html", rows=rows, cash=cash, total=total)

    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)

        symbol = request.form.get("symbol")

        if not lookup(symbol):
            return apology("must provide a valid symbol", 400)

        if not request.form.get("shares"):
            return apology("must provide shares", 400)

        if not request.form.get("shares") > 0:
            return apology("must provide a positive shares", 400)

        id = session["user_id"]

        rows = db.execute("SELECT id FROM users WHERE id = ?", id)

        if len(rows) != 1 :
            return apology("invalid user", 403)

        cash = db.execute("SELECT cash FROM users WHERE id = ?", id)

        if not cash >= request.form.get(price) * request.form.get(shares):
            return apology("not enough cash", 403)

        cash = cash - request.form.get(price) * request.form.get(shares)

        db.execute("UPDATE users SET cash = ?", cash)

        db.execute("UPDATE purchases SET symbol = ?, shares = ?", request.form.get("symbol"), request.form.get("shares"))

        return render_template("buy.html")

    else:
        return render_template("buy.html")
    return apology("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":

        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)

        symbol = request.form.get("symbol")

        if not lookup(symbol):
            return apology ("must provide correct symbol", 400)

        temp = lookup(symbol)

        symbol = temp["symbol"]
        price = temp["price"]

        return render_template("quoted.html", symbol=symbol, price=price)

    else:
        return render_template("quote.html")

    return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username", 400)
        if not request.form.get("password"):
            return apology("must provide password", 400)
        if not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username doesn't already exist
        if len(rows) == 1:
            return apology("username already exists", 400)

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("invalid password/confirmation", 400)

        password_hash = generate_password_hash(request.form.get("password"))
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), password_hash)

        if len(rows) == 1 and check_password_hash(rows[0]["hash"], request.form.get("password")):
            session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("register.html")

    return apology("TODO")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":

        return render_template("sell.html")

    else:
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)

        if not request.form.get("shares"):
            return apology("must provide password", 403)

        row = db.execute("SELECT symbol FROM purchases WHERE symbol = ?", request.form.get("symbol"))
        if not len(row) != 1:
            return apology("must provide correct symbol", 403)

        row = db.excute("SELECT shares FROM purchases WHERE symbol = ?", request.form.get("symbol"))
        if not request.form.get("shares") <= row:
            return apology("must provide correct shares", 403)

        cash = db.execute("SELECT cash FROM users")
        cash = cash + request.form.get("shares") * lookup(price)
        db.execute("UPDATE users SET cash = ?", cash)

        db.execute("UPDATE sell SET symbol = ?, shares = ?", request.form.get("symbol"), request.form.get("shares"))

        return render_templates("/")
    return apology("TODO")
