Pocket-Personal-Trainer ([Demo](https://www.youtube.com/watch?v=suKZ7QD2wX8))

## Project Overview (TLDR)
Pocket Personal Trainer is a Flask application that creates custom workouts based on functional movement training. This kind of training works several muscle groups at once so you build strength holistically. The app features an internally built library of 200 movements that can be selected from when creating or logging workouts. The included movements span across 7 movement patterns - pushing, pulling, hinging, squating, lunging, rotating, and gait. App features include account creation and login, selecting the body region for which you’d like to create a workout, a responsive display for browsing the movement library, a Javascript filter/search list to access a particular movement with user input, ability to select movements, sets, and repetitions for a given workout, accessing and displaying saved workouts from user page, and the logging of a previously completed workout in order to create a well-balanced follow-up workout. 

**Tech Stack 
Python, Flask, Javascript, AJAX, PostgreSQL, SQLAlchemy, HTML, Jinja, Bootstrap

**Links
[Demo with Voiceover](https://www.youtube.com/watch?v=suKZ7QD2wX8) |
[LinkedIn](https://www.linkedin.com/in/mollycstark/)

**About Pocket Personal Trainer

By filtering workout movements according to body region and function movement patterns, Pocket Personal Trainer automates the creation of effective training plans for weightlifting. The create workout functionality displays up to 200 movements that can be selected from to add to a user’s workout. The movements are stored in a JSON file containing movement name, a reference image, movement pattern name, and body region. A seed_database script iterates over the movements to instantiate them in the database. 

Pocket Personal Trainer is a Flask app that creates custom workouts based on functional movement training. The app features an internally built library of 200 movements that can be selected from when creating or logging workouts. App features include: account creation and login, selecting the body region for which you’d like to create a workout, a responsive display for browsing the movement library, a Javascript filter/search list to access a particular movement with user input, ability to select movements, sets, and repetitions for a given workout, accessing and displaying saved workouts from user page, and the logging of a previously completed workout in order to create a well-balanced follow-up workout.     

** Features

** Complex Data Model
Designed a complex data model to keep track of users, workouts, movements, workout movements, completed movements, and movement patterns. Data model connects users to their workouts - which store user selected workout movements - and completed movements. Data model connects movements to movement patterns, completed movements, and workout movements. This allows the app to suggest effective movements for user workouts based on which movement patterns a user should still target in their training plan.

** Create a Workout Utilizing Internally Built Library
Upon creating an account and logging in, the user can select Create Workout from the home page. This feature passes in the user’s id from session to create a workout in the Postgres database. The user’s body region submission is passed to a SQLAlchemy crud function that queries the database for movements matching the user’s selection. The movements are instantiated in the database with a seed-database script that loads  an internally built library of 200 movements, stored in a JSON file. The JSON file stores key information on each movement - the name, a reference image, the movement pattern, along with the body region the movement targets.

** Easily Access Movements with Filter Search List
I used a Javascript filter search list to grab user input from the DOM and hide movements that don’t match the search query. The onkeyup event occurs when the user releases a key on the keyboard while typing into the single-line text field with a placeholder value of “Search for movements.” A for loop iterates over the movement objects displaying only those with names that match the user’s input in the text field making it easier for the user to efficiently select desired movements from the library of 200.

** Mobile First Responsive Layout
I utilized Bootstrap’s grid system to create a responsive layout viewable on desktop, tablet, and mobile devices. Specifying the number of columns per row allowed me to vary the number of movement reference images displayed depending on the size of the user’s screen. On a desktop display 4 columns display 4 movement images per row, while 2 images are displayed per row on tablet, and 1 per row on mobile devices.

** Streamlined User Experience with Dynamic Display 
When the user clicks a movement, an AJAX request passes the movement name to the server. A crud function obtains the user object by passing in their username stored in session. The workout object is then obtained by getting that user’s last instantiated workout.  A workout movement is then added to the user’s workout without hard refreshing the page. The user can then add the desired sets and reps to each movement. Initially setting reps and sets to Nullable in model.py allows the user to update these values after the workout movement object has already been created in the database. 

** Saving Workouts
The user can create multiple workouts and access them via the navbar. A Jinja loop iterates over the user’s workouts passed from the server to the HTML template. Each loop generates a dynamic URL that renders that workout’s movements when clicked. 

** Logging Completed Movements
If a user has already trained pulling and hip hinge patterns with lat pull downs and deadlifts, logging these movements as “completed” will filter out any pulling and hip hinging movements when they create a new workout. The app will suggest movements that should still be targeted for balanced training - squatting, lunging, pushing, rotation, and gait. Selecting Clear Completed movements will trigger the deletion of that user’s completed movements to remove the filter.

**Installation

Requirements:
PostgreSQL
Python 3.7.3

To have this app running on your local computer, please follow the below steps:

Clone repository:
$ git clone https://github.com/mollycstark/Pocket-Personal-Trainer.git


Create and activate a virtual environment:
$ pip3 install virtualenv
$ virtualenv env
$ source env/bin/activate


Install dependencies:
(env) $ pip3 install -r requirements.txt

Create database and instantiate library of movements:
(env) $ python3 seed_database.py

Start backend server:
(env) $ python3 server.py

In an incognito web browser, navigate to port 5000 on localhost:
$ http://localhost:5000/




