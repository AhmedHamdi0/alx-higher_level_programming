#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def get_cities(username, password, db_name):
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=db_name)
        cursor = db.cursor()
        query = "SELECT * FROM cities ORDER BY id ASC"
        cursor.execute(query)

        states = cursor.fetchall()
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)
    finally:
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".
              format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    get_cities(username, password, db_name)
