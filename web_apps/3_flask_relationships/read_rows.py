from models import db, app, Puppy, Owner, Toy


with app.app_context():
    stmt = db.select(Puppy)
    results = db.session.execute(stmt).scalars()
    for row in results:
        print(row)