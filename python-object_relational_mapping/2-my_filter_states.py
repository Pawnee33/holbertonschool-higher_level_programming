#!/usr/bin/python3
"""
Module that connects to a MySQL database and lists states
whose name matches a user provided argument, ordered by id.
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
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC".format(sys.argv[4])
    )

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
