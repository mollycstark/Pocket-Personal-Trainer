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


@app.route("/api/select_movements")
def select_movements():
    """Instantiate user selected movements for a workout."""

    user = crud.get_user_by_username(session["user_username"])
    users_workout = crud.get_workout_by_user_id(user.user_id)

    movement_name = request.args.get("movement_name")
    movement_object = crud.get_movement_by_name(movement_name)

    workout_movement = crud.create_workout_movement(users_workout, movement_object)
    db.session.add(workout_movement)
    db.session.commit()

    return ('', 204)


@app.route("/display_workout")
def display_workout():
    """Display a user's workout."""

    user = crud.get_user_by_username(session["user_username"])
    workout = crud.get_workout_by_user_id(user.user_id)
    workout_movements = workout.workout_movements

    return render_template("display_workout.html", workout_movements=workout_movements)    


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
