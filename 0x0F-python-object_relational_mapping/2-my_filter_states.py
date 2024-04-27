#!/usr/bin/env python3

import sys
import MySQLdb

if __name__ == "__main__":
    # Get the command line arguments
    if len(sys.argv) != 5:
        print("Usage: ./script_name <username> <password> <database> <state_name>")
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Prepare the SQL query to fetch states matching the given name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    
    # Execute the query with the provided state_name
    cursor.execute(query, (state_name,))

    # Fetch all results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
