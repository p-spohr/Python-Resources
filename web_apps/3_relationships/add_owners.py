from models import db, app, Puppy, Owner, Toy



with app.app_context():
    bob = Owner('Bob', None)
    stmt = db.select(Puppy).where(Puppy.id == 1)
    puppy = db.session.execute(stmt).one()[0]
    bob.puppy_id = puppy.id
    puppy.owner = bob
    db.session.commit()
    