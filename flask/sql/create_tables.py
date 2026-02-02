from database.orm import db, Puppy, app
import sqlalchemy


with app.app_context():
    db.create_all()