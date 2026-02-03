from database.orm import db, Puppy, app
import sqlalchemy
import sys

stmt = db.select(Puppy)
print(stmt)

stmt2 = sqlalchemy.text(
    'SELECT * FROM puppy WHERE puppy.name LIKE :pattern'
)
print(stmt2)

stmt3 = db.select(Puppy).where(Puppy.name.like('%a%'))
print(stmt3)

stmt4 = db.select(Puppy).where(Puppy.name.contains('a'))
print(stmt4)

# sys.exit(1)

with app.app_context():
    
    results = db.session.execute(stmt).scalars()
    for row in results:
        print(row)
    
    # stmt2 = sqlalchemy.select(Puppy)
    # print(stmt2)
    # rows = db.session.execute(stmt).scalars()
    # for row in rows:
    #     print(row)
    
    # results = db.session.execute(stmt2.bindparams(pattern= '%a%')).scalars()
    results = db.session.execute(stmt4).scalars()
    for row in results:
        print(row)