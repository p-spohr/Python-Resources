from database.orm import db, Puppy, app
import sqlalchemy

stmt = sqlalchemy.delete(Puppy)
print(stmt)

with app.app_context():
    rows = db.session.execute(stmt)
    db.session.commit()
 