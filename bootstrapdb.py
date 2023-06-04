
from faker import Faker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import session

from models import Category, FilmCategory, Base
# from models import Base, Category, FilmCategory, Film, Language, Inventory, Rental
# from models import FilmActor, Actor, Customer, Payment, Address, Staff, City, Country, Store

from session import session


def generate_categories(session, count=10):
    fake = Faker()
    session.add_all([
        Category(
            name=fake.name()
        )
        for _ in range(count)
    ])
    session.commit()


def generate_film_category(session, count=10):
    fake = Faker()
    for category in session.query(Category):
        category.filmCategories.extend([
            FilmCategory(
                title=fake.sentence()
            )
            for _ in range(count)
        ])
    session.commit()

# def generate_actors(session, count=10):
#     fake = Faker()
#     session.add_all([
#         Actor(
#             first_name=fake.first_name(),
#             last_name=fake.last_name(),
#         )
#         for _ in range(count)
#     ])
#     session.commit()

def main():
    print("Creating database tables...")

    # Create database tables
    Base.metadata.create_all()

    print("Generating authors...")

    # Generate authors
    generate_categories(session)

    print("Generating articles...")
    # Generate articles
    generate_film_category(session)



    print("Done!")


if __name__ == "__main__":
    main()