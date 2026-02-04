
# Initiate the database and creates migrations folder
1. set environment variable FLASK_APP= <app_name.py>
2. run command in folder with file in FLASK_APP
```
flask db init
```

# Commit the current database and create version
```
flask db migrate -m "<message>"
```
Make sure to do an "initial migration"!

# Run the latest migration version to create database
```
flask db upgrade
```
upgrade() can be found under migrations/versions