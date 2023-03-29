# Pocket-Personal-Trainer
Known Issues: 

Completed movements
- If user logs completed movements at any point, the server will always route them to create workout b even if now they'd like to make an unrelated workout; have user drop completed movements by clearing logged movements prior to creating a new workout (see SQL Alchemy notes on deleting a record from the database)

Create workout b
- Should workout b hit body region form? Yes or no

User errors
- Check for any possible out of order clicking that could break application

Display workout
- Needs to display reps/sets
