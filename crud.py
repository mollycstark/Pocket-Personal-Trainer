"""CRUD operations."""

from model import db, User, Movement, CompletedMovement, MovementPattern, Workout, WorkoutMovement, connect_to_db


def create_user(username, password):
    """Create and return a new user."""

    user = User(
        username=username, 
        password=password
        )

    return user


def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_username(username):
    """Return a user by username."""

    return User.query.filter(User.username == username).first()


def create_movement(name, reference_image, movement_pattern):
    """Create and return a new movement."""

    movement = Movement(
        name=name,
        reference_image=reference_image,
        movement_pattern=movement_pattern,
        )

    return movement


def get_movements():
    """Return all movements."""

    return Movement.query.all()


def get_movement_by_id(movement_id):
    """Return a movement by primary key."""

    return Movement.query.get(movement_id)


def get_movement_by_name(name):
    """Return a movement by primary key."""

    return Movement.query.filter(Movement.name == name).first()


def create_completed_movement(movement, user, completed_at):
    """Create and return a new completed movement."""

    completed_movement = CompletedMovement(
        movement=movement,
        user=user, 
        completed_at=completed_at
        )

    return completed_movement


def get_completed_movements():
    """Return all completed movements."""

    return CompletedMovement.query.all()


def get_completed_movement_by_id(completed_movement_id):
    """Return a completed movement by primary key."""

    return CompletedMovement.query.get(completed_movement_id)


def create_movement_pattern(name):
    """Create and return a new movement pattern."""

    movement_pattern = MovementPattern(
        name=name
        )

    return movement_pattern


def get_movement_patterns():
    """Return all movement patterns."""

    return MovementPattern.query.all()


def get_movement_pattern_by_id(movement_pattern_id):
    """Return a movement pattern by primary key."""

    return MovementPattern.query.get(movement_pattern_id)


def get_movement_pattern_by_name(name):
    """Return a movement pattern by name."""

    return MovementPattern.query.filter(MovementPattern.name == name).first()


def create_workout(user):
    """Create and return a new workout."""

    workout = Workout(
        user=user
        )

    return workout


def get_workouts():
    """Return all workouts."""

    return Workout.query.all()


def get_workout_by_id(workout_id):
    """Return a workout by primary key."""

    return Workout.query.get(workout_id)


def get_workout_by_user_id(user_id):
    """Return a workout by user id."""

    return Workout.query.filter(Workout.user_id == user_id).first()


def create_workout_movement(workout, movement):
    """Create and return a new workout movement."""

    workout_movement = WorkoutMovement(
        workout=workout,
        movement=movement
        )

    return workout_movement


def get_workout_movements():
    """Return all workout movements."""

    return WorkoutMovement.query.all()


def get_workout_movement_by_id(workout_movement_id):
    """Return a workout movement by primary key."""

    return Workout.query.get(workout_movement_id)


if __name__ == "__main__":
    from server import app

    connect_to_db(app)