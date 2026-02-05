from models import db, app, Puppy, Owner, Toy

with app.app_context():
    puppy_id = 1
    red_ball = Toy('Chew Toy', puppy_id)
    stmt = db.select(Puppy).where(Puppy.id == puppy_id)
    puppy = db.session.execute(stmt).one()[0]
    puppy.toys.append(red_ball)
    db.session.commit()