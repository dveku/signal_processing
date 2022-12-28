import sqlite3

conn=sqlite3.connect('finalize.db')

cr=conn.cursor()

#Tempo
# try:
#     cr.execute("UPDATE feature SET Valence=Valence+1 WHERE tempo>80")
#     cr.execute("UPDATE feature SET Arousal=Arousal+1 WHERE tempo>80")
#     print("1-tempo updated")
# except:
#     print("Error with tempo")



conn.commit()
conn.close()