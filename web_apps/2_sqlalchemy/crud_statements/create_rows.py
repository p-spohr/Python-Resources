from database.orm import db, Puppy, app

# manual request when app not running
with app.app_context():
    # creates tables in model
    db.create_all()
    
    puppies= [
        Puppy('Rufus', 2),
        Puppy('Snow', 4),   
        Puppy('Sammy', 4),  
        Puppy('Frankie', 1),
    ]

    # one at a time
    # db.session.add(Puppy('Sammy', 4))
    # many at a time
    db.session.add_all(puppies)

    # commit changes (part of good transaction practice)
    # INSERT INTO, UPDATE, DELETE require commit to change database
    db.session.commit()

