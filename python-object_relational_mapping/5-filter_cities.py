#!/usr/bin/python3
"""
Script that connects to a MySQL database and lists all cities
of a given state provided as an argument, ordered by city id.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states "
        "ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id",
        (sys.argv[4],)
    )

    results = cursor.fetchall()

    cities = [row[1] for row in results]
    print(", ".join(cities))

    cursor.close()
    db.close()
