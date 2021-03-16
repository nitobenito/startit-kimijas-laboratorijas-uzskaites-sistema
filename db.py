import sqlite3
import requests, json
conn = sqlite3.connect('Dati.db')
c = conn.cursor()
#c.execute('CREATE TABLE IF NOT EXISTS Inventars (ID INTEGER PRIMARY KEY, NOSAUKUMS TEXT, TIPS TEXT, APAKSTIPS TEXT, SKAITS INTEGER, KOMENTARI TEXT)')
#c.execute("INSERT INTO Inventars (NOSAUKUMS, TIPS, APAKSTIPS, SKAITS, KOMENTARI) VALUES ('Mērkolba','Trauks','Mērtrauks',2,'Trauks ar tiplumu 300ml, kas paredzēts šķidrumu mērīšanai')")
#c.execute("DELETE FROM Inventars WHERE ID > 1")
#inventars_api_res = requests.get('https://pytonc.eu.pythonanywhere.com/api/v1/inventars')
#inventars = inventars_api_res.json()
#print(inventars)
#for inv in inventars:
    #c.execute("INSERT INTO Inventars (ID, NOSAUKUMS, TIPS, APAKSTIPS, SKAITS, KOMENTARI) values (?, ?, ?, ?, ?, ?)", [inv['id'], inv['nosaukums'], inv['tips'], inv['apakstips'], inv['skaits'], inv['komentari']])
#c.execute("UPDATE Inventars SET APAKSTIPS = 'Trauks' WHERE ID = 1")
#t = ('Trauks','Trauki',)
#c.execute('SELECT * FROM Inventars WHERE TIPS IN (?,?)', t)
#
#c.execute("SELECT * FROM Inventars")
c.execute('CREATE TABLE IF NOT EXISTS Users (id TEXT RIMARY KEY, vards TEXT, uzvards TEXT, loma TEXT, parole TEXT, Komentāri TEXT)')
users_json = json.load(open('dati/users.json'))
kolonas = ['id', 'vards', 'uzvards', 'loma', 'parole', 'Komentāri']
for data in users_json['users']:
  dati = tuple( data[c] for c in kolonas)
  c.execute("INSERT INTO  Users values (?,?,?,?,?,?)", dati)
c.execute("SELECT * FROM Users")
print(c.fetchall())

conn.commit()
c.close()
conn.close()
