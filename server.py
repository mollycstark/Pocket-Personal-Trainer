"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")


@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    username = request.form.get("username")
    password = request.form.get("password")

    user = crud.get_user_by_username(username)
    if user:
        flash("Cannot create an account with that username. Try again.")
    else:
        user = crud.create_user(username, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    username = request.form.get("username")
    password = request.form.get("password")

    user = crud.get_user_by_username(username)
    if not user or user.password != password:
        flash("The username or password you entered was incorrect.")
    else:
        # Log in user by storing the user's username in session
        session["user_username"] = user.username
        flash(f"Welcome back, {user.username}!")

    return redirect("/")


@app.route("/users")
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template("all_users.html", users=users)


@app.route("/create_workout")
def create_workout():
    """Create a workout."""

    movements = crud.get_movements()

    user = crud.get_user_by_username(session["user_username"])
    workout = crud.create_workout(user)
    db.session.add(workout)
    db.session.commit()
    flash("Workout created! Please select movements.")

    return render_template("all_movements.html", movements=movements)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
