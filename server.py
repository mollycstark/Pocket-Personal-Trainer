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


@app.route("/api/log_workout")
def log_workout():
    """Instantiate completed movements."""

    user = crud.get_user_by_username(session["user_username"])

    movement_name = request.args.get("movement_name")
    movement_object = crud.get_movement_by_name(movement_name)

    completed_movement = crud.create_completed_movement(movement_object, user)
    db.session.add(completed_movement)
    db.session.commit()

    return ('', 204)


@app.route("/create_workout_b")
def create_workout_b():
    """Create a follow up workout."""

    user = crud.get_user_by_username(session["user_username"])
    workout = crud.create_workout(user)
    db.session.add(workout)
    db.session.commit()

    all_movements = crud.get_movements()
    all_completed_movements = crud.get_completed_movements()
    
    completed_movement_patterns = []
    uncompleted_movements = []

    for completed_movement in all_completed_movements:
        completed_movement_patterns.append(completed_movement.movement.movement_pattern)


    for movement in all_movements:
            if movement.movement_pattern not in completed_movement_patterns:
                uncompleted_movements.append(movement)
         
    movements = uncompleted_movements

    return render_template("create_workout.html", movements=movements, workout=workout)


@app.route("/body_region")
def get_user_input():
    """User inputs body region focus for workout."""

    return render_template("body_region.html")


@app.route("/create_workout")
def create_workout():
    """Create a workout."""

    if crud.get_completed_movements():

        flash("Workout created! Please select movements.")

        return redirect("/create_workout_b")

    else:
        user_input = request.args.get("body-region")

        if user_input == "Full":
            movements = crud.get_movements()

        else:
            movements = crud.get_movements_by_body_region(user_input) 

        user = crud.get_user_by_username(session["user_username"])
        workout = crud.create_workout(user)
        db.session.add(workout)
        db.session.commit()
        flash("Workout created! Please select movements.")

    return render_template("create_workout.html", movements=movements, workout=workout)


@app.route("/all_movements")
def all_movements():
    """Display all movements."""

    movements = crud.get_movements()

    return render_template("log_workout.html", movements=movements)


@app.route("/api/select_movements")
def select_movements():
    """Instantiate user selected movements for a workout."""

    user = crud.get_user_by_username(session["user_username"])
    users_workout = crud.get_last_workout_by_user_id(user.user_id)

    movement_name = request.args.get("movement_name")
    movement_object = crud.get_movement_by_name(movement_name)

    workout_movement = crud.create_workout_movement(users_workout, movement_object)
    db.session.add(workout_movement)
    db.session.commit()

    return ('', 204)


@app.route("/display_workout/<workout_id>")
def display_workout(workout_id):
    """Display a user's workout."""

    workout = crud.get_workout_by_id(workout_id)
    workout_movements = workout.workout_movements

    return render_template("display_workout.html", workout_movements=workout_movements)    


@app.route("/view_workouts")
def view_workouts():
    """Display a user's saved workouts."""

    user = crud.get_user_by_username(session["user_username"])
    workouts = crud.get_all_workouts_by_user_id(user.user_id)

    return render_template("view_workouts.html", workouts=workouts)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
