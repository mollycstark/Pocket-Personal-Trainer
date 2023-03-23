"""Script to seed database."""

import os
import json


import crud
import model
import server


os.system("dropdb workouts")
os.system("createdb workouts")

model.connect_to_db(server.app)
model.db.create_all()


# Load movement patterns data from JSON file
with open("data/movement_patterns.json") as f:
    movement_patterns = json.loads(f.read())

# Create movement patterns 
# Store them in list to instantiate movement pattern records
movement_patterns_in_db = []
for movement_pattern in movement_patterns:
    name = (
        movement_pattern["name"]
    )

    db_movement_pattern = crud.create_movement_pattern(name)
    movement_patterns_in_db.append(db_movement_pattern)

model.db.session.add_all(movement_patterns_in_db)
model.db.session.commit()


# Load movements data from JSON file
with open("data/movements.json") as f:
    movement_data = json.loads(f.read())

# Create movements 
# Store them in list to instantiate movement records
movements_in_db = []
for movement in movement_data:
    name, reference_image, movement_pattern, body_region = (
        movement["name"],
        movement["reference_image"],
        crud.get_movement_pattern_by_name(movement["movement_pattern"]),
        movement["body_region"],
    )

    db_movement = crud.create_movement(name, reference_image, movement_pattern, body_region)
    movements_in_db.append(db_movement)

model.db.session.add_all(movements_in_db)
model.db.session.commit()

