#!/usr/bin/python3
"""
Module that connects to a MySQL database and lists all cities
with their corresponding state name, ordered by city id.
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
        "ORDER BY cities.id"
    )

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
