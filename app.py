from flask import Flask, render_template, request, session, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = "workshop-secret"
DB = "menu.db"


def get_db():
    return sqlite3.connect(DB)


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT,
            password TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS menu (
            name TEXT,
            price REAL
        )
    """)

    if conn.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 0:
        conn.execute("INSERT INTO users VALUES ('admin', '1234')")

    if conn.execute("SELECT COUNT(*) FROM menu").fetchone()[0] == 0:
        conn.execute("INSERT INTO menu VALUES ('Dosa', 40)")
        conn.execute("INSERT INTO menu VALUES ('Idli', 30)")

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    # TODO: Get username and password from request.form
    # TODO: Check the users table
    # TODO: If the credentials are correct, store the login in session
    return "TODO: Implement login"


@app.route("/menu")
def menu():
    if not session.get("admin"):
        return redirect("/")

    conn = get_db()
    items = conn.execute("SELECT * FROM menu").fetchall()
    conn.close()

    return render_template("menu.html", items=items)


@app.route("/add-item", methods=["POST"])
def add_item():
    # TODO: Get name and price from request.form
    # TODO: INSERT the item into the menu table
    # TODO: Commit the change
    return "TODO: Implement add-item"


init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
