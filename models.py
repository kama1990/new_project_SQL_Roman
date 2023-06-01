import datetime

from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
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


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False, unique=True)
    description = Column(String(200))
    release_year = Column(Integer)
    language_id = Column(Integer, nullable=False, unique=True)  # connect with language
    rental_duration = Column(Integer)
    length = Column(String(50))
    replacement_cost = Column(Integer)
    rating = Column(Integer)

    last_update = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )  # connect with all without Payments

    special_features = Column(String(100))
    fulltext = Column(Text)


class Language(Base):
    __tablename__ = "languages"

    language_id = Column(
        Integer,
        ForeignKey("films.language_id"),
        primary_key=True,
        nullable=False,
        unique=True
    )
    name = Column(String(200))
    last_update = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )


class Inventory(Base):
    __tablename__ = "inventories"

    inventory_id = Column(Integer, primary_key=True)

    film_id = Column(
        Integer,
        ForeignKey("films.id"),
        nullable=False,
        unique=True
    )

    store_id = Column(Integer)
    last_update = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )


class Rental(Base):
    __tablename__ = "rentals"

    rental_id = Column(Integer, primary_key=True)
    rental_date = Column(Integer)
    inventory_id = Column(
        Integer,
        ForeignKey("inventories.inventory_id")
    )
    customer_id = Column(Integer, nullable=False, unique=False)
    return_date = Column(Integer)
    stuff_id = Column(Integer)

    last_update = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now()
    )


class FilmActor(Base):
    __tablename__ = "film_actors"

    actor_id = Column(Integer, primary_key=True)

    film_id = Column(
        Integer,
        ForeignKey("films.id"),
        nullable=False,
        unique=True
    )
    last_update = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )


class Actor(Base):
    __tablename__ = "actors"

    actor_id = Column(
        Integer,
        ForeignKey("film_actors.actor_id"),
        primary_key=True,
        nullable=False,
        unique=True
    )
    first_name = Column(String(50))
    last_name = Column(String(50))

    last_update = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(
        Integer,
        ForeignKey("rentals.customer_id"),
        primary_key=True,
        nullable=False,
        unique=True
    )

    store_id = Column(
        Integer,
        ForeignKey("inventories.store_id")
    )

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    address_id = Column(String(100), nullable=False, unique=True)
    is_active = Column(String(20), nullable=False)
    create_date = Column(String(10))
    lastupdate = Column(String(10))

    rental_id = Column(
        Integer,
        ForeignKey("rentals.rental_id"))


class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, nullable=False)

    customer_id = Column(
        Integer,
        ForeignKey("customers.customer_id")
    )

    stuff_id = Column(
        Integer,
        ForeignKey("rentals.stuff_id")
    )

    rental_id = Column(
        Integer,
        ForeignKey("rentals.rental_id")
    )

    amount = Column(Integer)
    payment_date = Column(String(10))


class Address(Base):
    __tablename__ = "addresses"

    address_id = Column(
        Integer,
        ForeignKey("customers.customer_id"),
        primary_key=True
    )
    address = Column(String(100))
    address2 = Column(String(100))
    district = Column(String(100))
    city_id = Column(Integer)
    post_code = Column(Integer)
    phone = Column(Integer)
    last_update = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )


class Staff(Base):
    __tablename__ = "staff"

    staff_id = Column(
        Integer,
        ForeignKey("rentals.staff_id"),
        primary_key=True
    )

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    address_id = Column(Integer, nullable=False)

    store_id = Column(Integer)
    active = Column(String(20))
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(20), nullable=False)

    lastupdate = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )

    picture = Column(String(20))


class City(Base):
    __tablename__ = "cities"

    city_id = Column(
        Integer,
        ForeignKey("addresses.address_id"),
        primary_key=True,
        nullable=False,
        unique=True
    )

    city = Column(String(50))
    country_id = Column(Integer, nullable=False, unique=True)

    last_update = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )


class Country(Base):
    __tablename__ = "countries"

    country_id = Column(
        Integer,
        ForeignKey("cities.country_id"),
        primary_key=True,
        nullable=False,
        unique=True
    )

    country = Column(String(50))

    last_update = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )


class Store(Base):
    __tablename__ = "stores"

    store_id = Column(
        Integer,
        ForeignKey("staff.store.id"),
        primary_key=True
    )

    manager_staff_id = Column(Integer, nullable=False)
    address_id = Column(Integer)

    last_update = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now
    )
