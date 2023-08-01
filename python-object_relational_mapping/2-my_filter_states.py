#!/usr/bin/python3
"""Module that takes in an argument and displays all values in the states"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=argv[1], passwd=argv[2], db=argv[3])
    """Connecting to the MySQL server"""

    cursor = connection.cursor()
    """Creating a cursor object to execute queries"""

    cursor.execute("SELECT * FROM states "
                   "WHERE name='{}' ORDER BY states.id ASC".format(argv[4]))
    """Executing the SELECT query to retrieve all states"""

    lines = cursor.fetchall()
    """Fetching all the lines returned by the query"""

    for line in lines:
        """Display the results"""
        if line[1] == argv[4]:
            print(line)

    cursor.close()
    connection.close()
    """Closing the cursor and the connection"""
