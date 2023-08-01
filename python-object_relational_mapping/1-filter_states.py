#!/usr/bin/python3
"""Module that lists all states with a name starting with N"""

import MySQLdb
import sys


if __name__ == "__main__":
    connection = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                                 db=sys.argv[3])
    """Connecting to the MySQL server"""

    cursor = connection.cursor()
    """Creating a cursor object to execute queries"""

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    """Executing the SELECT query to retrieve all states"""

    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]
    """Display the results"""

    cursor.close()
    connection.close()
    """Closing the cursor and the connection"""
