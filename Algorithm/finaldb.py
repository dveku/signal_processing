import sqlite3
try:
    conn=sqlite3.connect('music.db')
    print("successfully connected to database!")
except:
    print("Error connecting to database")
    
cr=conn.cursor()

cr.execute("DROP COLUMN Valence")
conn.commit()
conn.close()