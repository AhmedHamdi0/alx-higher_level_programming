#!/usr/bin/python3
"""lists all cities of a state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def filter_cities(username, password, db_name, state_name):
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=db_name)
        cursor = db.cursor()

        query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
        cursor.execute(query, (state_name,))

        cities = cursor.fetchall()
        city_names = [city[0] for city in cities]
        print(', '.join(city_names))

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)
    finally:
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".
              format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name, state_name = (
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    filter_cities(username, password, db_name, state_name)
