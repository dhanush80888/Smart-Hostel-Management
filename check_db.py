import sqlite3, os
path='db.sqlite3'
print('exists', os.path.exists(path))
if os.path.exists(path):
    conn=sqlite3.connect(path)
    cur=conn.cursor()
    cur.execute("SELECT name, sql FROM sqlite_master WHERE type='table';")
    for row in cur.fetchall():
        print(row)
    # check columns
    cur.execute("PRAGMA table_info('hostel_weeklymenu')")
    print('columns', cur.fetchall())
    conn.close()
