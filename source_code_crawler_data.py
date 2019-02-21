import requests
from bs4 import BeautifulSoup
import sqlite3


src = "https://www.kompasiana.com/olahraga"

page = requests.get(src)


soup = BeautifulSoup(page.content, 'html.parser')

konten = soup.findAll(class_='timeline--artikel')

koneksi = sqlite3.connect('db_data.db')
koneksi.execute(''' CREATE TABLE if not exists kompasiana
            (judul TEXT NOT NULL,
             view TEXT NOT NULL,
             like TEXT NOT NULL,
             komen TEXT NOT NULL);''')

for i in range(len(konten)):

    judul = konten[i].find(class_='title')
    judul = judul.find('a').getText()

    statistik = konten[i].findAll(class_='artikel--count__item')
    view=statistik[0].getText()
    like=statistik[1].getText()
    komen=statistik[2].getText()

    koneksi.execute('''INSERT INTO kompasiana values ('%s', '%s', '%s', '%s');'''%(judul, view, like, komen));



tampil = koneksi.execute("SELECT * FROM kompasiana")
for row in tampil:
    print(row)

