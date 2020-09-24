#!/usr/bin/env python3

import sys, sqlite3, csv
from collections import defaultdict

from sqlite3 import Error
# RECORDS SCHEMA
# teamid name wins lost tied goals opgoals division char, foreign key(teamid) references teams(teamid)
def get_connection(fname):
    try:
        con = sqlite3.connect(fname)
        return con
    except Error as errmess:
        print(errmess)
        return None

if __name__ == "__main__":
    con = get_connection("something.db")
    if not con:
        print("Connect to: " + db + "failed!")
        sys.exit(0)

    cur = con.cursor()

    # example query
    query = "select * from table;"
    rows = cur.execute(query)
    
    # for row in rows:
    #     something
    con.commit()
    con.close()
