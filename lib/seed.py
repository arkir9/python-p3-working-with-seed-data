#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, Base  # Import the Game class and Base from the models module

fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///seed_db.db')
    Base.metadata.create_all(engine)  # Create all tables defined in the models
    Session = sessionmaker(bind=engine)
    session = Session()
    
    botw = Game(title="Breath of the Wild", platform="Switch", genre="Adventure", price=60)
    ffvii = Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30)
    mk8 = Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)

    session.bulk_save_objects([botw, ffvii, mk8])
    session.commit()

print("Seeding games...")

games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
for i in range(50)]

session.bulk_save_objects(games)
session.commit()