#!/usr/bin/python3
"""Module that lists cities states from the database"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2], db=argv[3])
    """Connecting to the MySQL server"""

    cursor = connection.cursor()
    """Creating a cursor object to execute queries"""

    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities LEFT JOIN states "
                   "ON cities.state_id=states.id WHERE states.name=%s "
                   "ORDER BY cities.id ASC", (argv[4],))
    """Executing the SELECT query to retrieve all cities"""

    lines = cursor.fetchall()
    """Fetching all the lines returned by the query"""

    print(', '.join([line[1] for line in lines]))
    """Display the results"""

    cursor.close()
    connection.close()
    """Closing the cursor and the connection"""
