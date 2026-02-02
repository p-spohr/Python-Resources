from database.orm import db, Puppy, app
import sqlalchemy

# stmt = sqlalchemy.text("DROP TABLE puppies")
# print(stmt)

with app.app_context():
    # drop the table
    print(db.engine)
    Puppy.__table__.drop(db.engine)
    
    # puppy_table = sqlalchemy.Table(Puppy.__tablename__, db.metadata, autoload_with= db.engine)
    # print(puppy_table)
    # puppy_table.drop(db.engine, checkfirst= True)
 