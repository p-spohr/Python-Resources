from database.orm import db, Puppy, app
import sqlalchemy
import sys


with app.app_context():
    
    stmt = Puppy.query.filter_by(name= 'Snow')
    print(stmt)
    pup = db.session.execute(stmt)
    print(pup.scalar())
