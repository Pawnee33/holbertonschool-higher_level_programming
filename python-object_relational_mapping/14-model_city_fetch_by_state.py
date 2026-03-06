#!/usr/bin/python3
"""Module that connects to a MySQL database and displays all cities
with their associated state name using SQLAlchemy."""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (
        session.query(State, City)
        .filter(State.id == City.state_id)
        .order_by(City.id)
    )

    for state, city in cities:
        print("{}: {} {}".format(state.name, city.id, city.name))
