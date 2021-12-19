#!/usr/bin/python3
""" module containing a script for listing states"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM states RIGHT JOIN cities\
                ON states.id=cities.state_id\
                WHERE states.name= %s ORDER BY cities.id ASC", (sys.argv[4],))
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    db.close()
