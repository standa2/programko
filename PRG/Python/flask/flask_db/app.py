from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3, random

app = Flask(__name__)

DATABASE = "instance/database.db"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource("schema.sql", mode="r") as file:
            db.cursor().executescript(file.read())
        db.commit()

@app.teardown_appcontext
def close_connection(exeption):
    db = get_db()
    if db is not None:
        db.close()

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/bye")
def bye():
    return render_template("bye.html")

@app.route("/form", methods=["GET","POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        if len(name.split()) <= 1:
            name = "error"
        if len(name.split()) > 1:
            name = name.title()
        input_class = request.form.get("input_class")
        if len(input_class) >= 3:
            input_class = "error"
        message = request.form.get("message")
        grade = random.randint(1,5)
        cursor = get_db().cursor()
        cursor.execute(
            f"INSERT INTO students (student_name, class, student_message, grade) VALUES (?, ?, ?, ?)", (name, input_class, message, grade)
        )
        get_db().commit()
    
    return render_template("form.html")

@app.route("/result")
def result():
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    return render_template("result.html",  rows=rows)
    



if __name__ == "__main__":
    init_db()
    app.run(debug=True)