"""Models for workout app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# -------------------------------------------------------------------
# Part 1: Compose ORM

class User(db.Model):
    """Web application user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)

    completed_movements = db.relationship("CompletedMovement", back_populates="user")
    workouts = db.relationship("Workout", back_populates="user")

    def __repr__(self):
        """Provide useful output when printing."""

        return f"<User {self.username} user_id={self.user_id}>"


class Movement(db.Model):
    """Movement."""

    __tablename__ = "movements"

    movement_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String, nullable=False)
    reference_image = db.Column(db.String, nullable=False)
    movement_pattern_id = db.Column(db.Integer, db.ForeignKey('movement_patterns.movement_pattern_id'), nullable=False)
    body_region = db.Column(db.String, nullable=False)

    completed_movements = db.relationship("CompletedMovement", back_populates="movement")
    movement_pattern = db.relationship("MovementPattern", back_populates="movements")
    workout_movements = db.relationship("WorkoutMovement", back_populates="movement")

    def __repr__(self):
        """Provide useful output when printing."""

        return f"<Movement {self.name} movement_id={self.movement_id}>"


class CompletedMovement(db.Model):
    """Completed movement."""

    __tablename__ = "completed_movements"

    completed_movement_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    movement_id = db.Column(db.Integer, db.ForeignKey('movements.movement_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    # completed_at = db.Column(db.DateTime, nullable=False)

    movement = db.relationship("Movement", back_populates="completed_movements")
    user = db.relationship("User", back_populates="completed_movements")

    def __repr__(self):
        """Provide useful output when printing."""

        return f"<Completed Movement {self.movement.name} completed_movement_id={self.completed_movement_id}>"       


class MovementPattern(db.Model):
    """Movement pattern."""

    __tablename__ = "movement_patterns"

    movement_pattern_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String, nullable=False)

    movements = db.relationship("Movement", back_populates="movement_pattern")

    def __repr__(self):
        """Provide useful output when printing."""

        return f"<Movement Pattern {self.name} movement_pattern_id={self.movement_pattern_id}>"  


class Workout(db.Model):
    """Workout."""

    __tablename__ = "workouts"

    workout_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    user = db.relationship("User", back_populates="workouts")
    workout_movements = db.relationship("WorkoutMovement", back_populates="workout")

    def __repr__(self):
        """Provide useful output when printing."""

        return f"<Workout_id={self.workout_id}>"      
        

class WorkoutMovement(db.Model):
    """Workout movement."""

    __tablename__ = "workout_movements"

    workout_movement_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.workout_id'), nullable=False)
    movement_id = db.Column(db.Integer, db.ForeignKey('movements.movement_id'), nullable=False)

    workout = db.relationship("Workout", back_populates="workout_movements")
    movement = db.relationship("Movement", back_populates="workout_movements")

    def __repr__(self):
        """Provide useful output when printing."""

        return f"<Workout_movement_id={self.workout_movement_id}>"          

# End part 1
# -------------------------------------------------------------------
# Helper functions


def connect_to_db(flask_app, db_uri="postgresql:///workouts", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
