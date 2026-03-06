#!/usr/bin/python3
"""
Module that connects to a MySQL database and lists all states
with a name starting with 'N', and ordered by id from the states table.
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
        "SELECT id, name "
        "FROM states "
        "WHERE states.name LIKE 'N%' "
        "ORDER BY id ASC"
    )

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
