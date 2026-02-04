from database.orm import db, Puppy, app
import sqlalchemy

stmt = sqlalchemy.text("SELECT * FROM sqlite_master WHERE type='table'")
print(stmt)

with app.app_context():
    results = db.session.execute(stmt)
    for row in results:
        print(row)
    
    # stmt2 = sqlalchemy.select(Puppy)
    # print(stmt2)
    # rows = db.session.execute(stmt).scalars()
    # for row in rows:
    #     print(row)