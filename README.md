# Pocket-Personal-Trainer
Known Issues: 

Querying for more than one workout
- If user creates more than one workout application will always get the first workout; possible solution: store workout id in session and render that workout when hitting display workout button

Completed movements
- If user logs completed movements at any point, the server will always route them to create workout b even if now they'd like to make an unrelated workout
- If more than one user logs completed movements, application will not differentiate between different users completed movements; possible solution: get user's completed movements

User errors
- Clicking navigation out of order breaks application
- After they create a workout, etc. need functionality to navigate back to homepage or user page

Saved Workouts
- Don't render that workout from the database, need to do something with query string in URL for any routes that create a workout... or the route before that redirects to the route that creates a workout???