from models import db, app, Puppy, Owner, Toy


puppy_names = [
    'Brownie',
    'Snow',
    'Rainbow',
    'Bandit',
    'Floppy'
]

with app.app_context():
    puppies = [Puppy(name) for name in puppy_names]
    db.session.add_all(puppies)
    db.session.commit()
    
    
    