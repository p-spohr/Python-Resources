# %%

from basics import db, Puppy, app

# %%

# manual request when app not running
with app.app_context():
    # creates tables in model
    db.create_all()

    sammy = Puppy('Sammy', 3)
    frankie = Puppy('Frankie', 1)

    # db.session.add(sammy)
    db.session.add_all([sammy, frankie])

    db.session.commit()

    print(sammy.id, frankie.id)
    
    print(sammy)
    
    print(db.session.execute(db.select(Puppy.name).order_by(Puppy.name)).scalars().all())

# %%
