#!/usr/bin/env python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password dbname".format(sys.argv[0]))
        sys.exit(1)

    # Get the MySQL login credentials and the database name from the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    dbname = sys.argv[3]

    # Connect to MySQL database on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=dbname
    )

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    # Query to retrieve all states, sorted by id in ascending order
    query = "SELECT id, name FROM states ORDER BY id ASC"

    # Execute the query
    cur.execute(query)

    # Fetch all the results
    rows = cur.fetchall()

    # Print each row as "id, name"
    for row in rows:
        print(f"{row[0]}, {row[1]}")

    # Close the cursor and the database connection
    cur.close()
    db.close()
