from basics import db, Puppy, app

new_puppy = Puppy('Rufus', 5)

with app.app_context():
    db.create_all()
    all_pups = db.session.execute(db.select(Puppy).where(Puppy.id == 2))
    for pup in all_pups:
        print(pup[0].id, pup[0].name, pup[0].age)
        print(db.session.execute(db.select(Puppy.name, Puppy.age).where(Puppy.id == pup[0].id)).all())