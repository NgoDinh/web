from flask import Flask, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine("postgresql://postgres:postgres@localhost/mydatabase")
db = scoped_session(sessionmaker(bind=engine))

#-------------------------------------------------------------------------------
notes = []

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)

    return render_template("index_session.html", notes=notes)

@app.route("/flights")
def index_flights():
    flights = db.execute("select * from flights").fetchall()
    return render_template("index_flights.html", flights = flights)

@app.route("/flights/book", methods = ["POST"])
def book():
    name = request.form.get("name")
    flight_id = int(request.form.get("flight_id"))
    db.execute("Insert into passengers(flight_id, name) values (:flight_id, :name)",
        {"name":name, "flight_id":flight_id})
    db.commit()
    return("<h1>Success!!!</h1>")
