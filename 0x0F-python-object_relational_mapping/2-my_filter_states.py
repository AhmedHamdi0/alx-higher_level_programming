#!/usr/bin/python3
"""  displays all values in the states table of hbtn_0e_0_usa
 where name matches the argument. """
import MySQLdb
import sys


def get_states_match_name(username, password, db_name, state_name):
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=db_name)
        cursor = db.cursor()
        query = (f"""SELECT * FROM states WHERE
                 name LIKE BINARY '{state_name}' ORDER BY id ASC""")
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
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name, state_name = (
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    get_states_match_name(username, password, db_name, state_name)
