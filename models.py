import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from session import engine

Base = declarative_base(bind=engine)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)  # connect with FILM
    name = Column(String(100))

    last_update = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )  # connect with all without Payments

    # category z fimCategory 1 do 1

    filmCategories = relationship("FilmCategory", cascade="all, delete, delete-orphan")
    def __repr__(self):
        return f"Category({self.name})"


class FilmCategory(Base):
    __tablename__ = "filmCategories"

    film_id = Column(Integer, primary_key=True)  # connect with Inventory, FilmActor,
    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False)

    last_update = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )  # connect with all without Payments
    title = Column(String(100))
    # film Category z Category - 1 do 1
    # fimCategory  z Film 1 do 1

    category = relationship("Category")

# class Film(Base):
#     __tablename__ = "films"
#
#     id = Column(Integer, primary_key=True, nullable=False, unique=True)
#     title = Column(String(200), nullable=False, unique=True)
#     description = Column(String(200))
#     release_year = Column(Integer)
#     language_id = Column(Integer, nullable=False, unique=True)  # connect with language
#     rental_duration = Column(Integer)
#     length = Column(String(50))
#     replacement_cost = Column(Integer)
#     rating = Column(Integer)
#
#     last_update = Column(
#         DateTime,
#         nullable=False,
#         default=datetime.datetime.now
#     )  # connect with all without Payments
#
#     special_features = Column(String(100))
#     fulltext = Column(Text)
#
#     # Film z FilmCategory 1 do 1
#     # Film z Inventory wiele do 1
#     # Film z Film actor wiele do 1
#     # Film z Language wiele do 1
#
#
#
#     def __repr__(self):
#         return f"Film({self.title})"
#
#
# class Language(Base):
#     __tablename__ = "languages"
#
#     language_id = Column(
#         Integer,
#         ForeignKey("films.language_id"),
#         primary_key=True,
#         nullable=False,
#         unique=True
#     )
#     name = Column(String(200))
#     last_update = Column(
#         DateTime,
#         nullable=False,
#         default=datetime.datetime.now
#     )
#
#     # Language z Film - 1 do wielu
#
#     def __repr__(self):
#         return f"Language({self.name})"
#
#
# class Inventory(Base):
#     __tablename__ = "inventories"
#
#     inventory_id = Column(Integer, primary_key=True)
#
#     film_id = Column(
#         Integer,
#         ForeignKey("films.id"),
#         nullable=False,
#         unique=True
#     )
#
#     store_id = Column(Integer)
#     last_update = Column(
#         DateTime,
#         nullable=False,
#         default=datetime.datetime.now
#     )
#
#     # Inventory z Film - 1 do wielu
#     # Inventory z Rental - 1 do wielu
#
#
# class Rental(Base):
#     __tablename__ = "rentals"
#
#     rental_id = Column(Integer, nullable=False, primary_key=True)
#     rental_date = Column(Integer)
#     inventory_id = Column(
#         Integer,
#         ForeignKey("inventories.inventory_id")
#     )
#     customer_id = Column(
#         Integer
#     )
#
#     return_date = Column(Integer)
#     stuff_id = Column(Integer, nullable=False)
#
#     last_update = Column(
#         DateTime,
#         nullable=False,
#         default=datetime.datetime.now
#     )
#
#     # Rental z Inventor - wiele do 1
#     # Rental z Customer 1 do 1
#     # Rental z Payments 1 do wielu
#     # Rental z Staff wiele do 1
#
#
# class FilmActor(Base):
#     __tablename__ = "film_actors"
#
#     actor_id = Column(Integer, primary_key=True)
#
#     film_id = Column(
#         Integer,
#         ForeignKey("films.id"),
#         nullable=False,
#         unique=True
#     )
#     last_update = Column(
#         DateTime,
#         nullable=False,
#         default=datetime.datetime.now
#     )
#
#     # FilmActor z Film 1 do wielu
#     # FilmActor z Actor wiele do 1
#
#
# class Actor(Base):
#     __tablename__ = "actors"
#
#     actor_id = Column(
#         Integer,
#         ForeignKey("film_actors.actor_id"),
#         primary_key=True,
#         nullable=False,
#         unique=True
#     )
#     first_name = Column(String(50))
#     last_name = Column(String(50))
#
#     last_update = Column(
#         DateTime,
#         nullable=False,
#         default=datetime.datetime.now
#     )
#
#     # Actor z FilmActor 1 do wielu
#
#
# class Customer(Base):
#     __tablename__ = "customers"
#
#     customer_id = Column(
#         Integer,
#         # ForeignKey("rentals.customer_id"),
#         primary_key=True
#     )
#
#     store_id = Column(
#         Integer)
#         # ForeignKey("inventories.store_id"),
#         # nullable=False
#
#
#     first_name = Column(String(50), nullable=False)
#     last_name = Column(String(100), nullable=False)
#     email = Column(String(50), nullable=False, unique=True)
#     address_id = Column(String(100), nullable=False, unique=True)
#     is_active = Column(String(20), nullable=False)
#     create_date = Column(String(10))
#     last_update = Column(String(10))
#
#     rental_id = Column(
#         Integer)
#        # ForeignKey("rentals.rental_id"))
#
#     # Customer z Rental 1 do 1
#     # Customer z Address wiele do 1
#     # Customer z Payments 1 do wielu
#
#
# class Payment(Base):
#     __tablename__ = "payments"
#
#     payment_id = Column(Integer, primary_key=True, nullable=False)
#
#     customer_id = Column(
#         Integer,
#         ForeignKey("customers.customer_id"),
#         nullable=False
#     )
#
#     stuff_id = Column(
#         Integer)
#         #  ForeignKey("rentals.stuff_id"),
#         #  nullable=False
#
#     rental_id = Column(
#         Integer)
#         # ForeignKey("rentals.rental_id"),
#         # nullable=False
#
#
#     amount = Column(Integer)
#     payment_date = Column(String(10))
#
#     # Payment z Rental wiele do 1
#     # Payment with Customer wiele do 1
#     # Payments with Staff wiele do 1
#
#
# class Address(Base):
#     __tablename__ = "addresses"
#
#     address_id = Column(
#         Integer,
#         ForeignKey("customers.customer_id"),
#         primary_key=True
#     )
#     address = Column(String(100))
#     address2 = Column(String(100))
#     district = Column(String(100))
#     city_id = Column(Integer)
#     post_code = Column(Integer)
#     phone = Column(Integer)
#     last_update = Column(
#         DateTime,
#         nullable=False,
#         default=datetime.datetime.now
#     )
#
#     # Address with Customer jeden do wielu
#     # Address with City wiele do 1
#     # Address with Store 1 do wielu
#     # Address with Staff 1 do wielu
#
#
# class Staff(Base):
#     __tablename__ = "staff"
#
#     staff_id = Column(Integer, unique=True)
#     first_name = Column(String(50), nullable=False)
#     last_name = Column(String(50), nullable=False)
#     address_id = Column(
#         Integer,
#         ForeignKey("addresses.address_id"),
#         nullable=False)
#
#     store_id = Column(Integer, primary_key=True)
#     active = Column(String(20))
#     username = Column(String(20), nullable=False, unique=True)
#     password = Column(String(20), nullable=False)
#
#     last_update = Column(
#         DateTime,
#         nullable=False,
#         default=datetime.datetime.now
#     )
#
#     picture = Column(String(20))
#
#     # Staff with Address 1 do wielu
#     # Staff with Payments 1 do wielu
#     # Staff with Rental 1 do wielu
#     # Staff with Store 1 do 1
#
#
# class City(Base):
#     __tablename__ = "cities"
#
#     city_id = Column(
#         Integer,
#         ForeignKey("addresses.address_id"),
#         primary_key=True,
#         nullable=False,
#         unique=True
#     )
#
#     city = Column(String(50))
#     country_id = Column(Integer, nullable=False, unique=True)
#
#     last_update = Column(
#         DateTime,
#         nullable=False,
#         default=datetime.datetime.now
#     )
#
#     # City with Address 1 do wielu
#     # City with country wiele do 1
#
#
# class Country(Base):
#     __tablename__ = "countries"
#
#     country_id = Column(
#         Integer,
#         ForeignKey("cities.country_id"),
#         primary_key=True,
#         nullable=False,
#         unique=True
#     )
#
#     country = Column(String(50))
#
#     last_update = Column(
#         DateTime,
#         nullable=False,
#         default=datetime.datetime.now
#     )
#
#     # Country with City 1 do wielu
#
#
# class Store(Base):
#     __tablename__ = "stores"
#
#     store_id = Column(
#         Integer)
#         #ForeignKey("staff.store_id"),
#         #unique=True
#
#     manager_staff_id = Column(Integer, nullable=False, primary_key=True)
#     address_id = Column(Integer)
#
#     last_update = Column(
#         DateTime,
#         nullable=False,
#         default=datetime.datetime.now
#     )
#
#     # Store with Address wiele do 1
#     # Store with Staff 1 do 1
#
#
Base.metadata.create_all(engine)
