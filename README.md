# Crawler-Data-Website
mengambil data teks dari sebuah website

# Web Crawler Menggunakan Python



> Nama : Iis Yuni Harianti
>
> NIM : 160411100086

> Mata kuliah : Pengembangan dan Pencarian Web
>
> Dosen Pengampu : Mulaab, S.Si., M.Kom

------



Web Crawler digunakan untuk mengambil data berupa teks pada sebuah website.

Aplikasi yang dibutuhkan yaitu aplikasi python, pastikan sudah terinstall pada laptop.

Selanjutnya yang perlu dilakukan yaitu sebagai berikut :

1. Pada "Local Disk (C:)" carilah folder "python34" kemudian double klik folder tersebut.

2. Selanjutnya  cari folder "Scripts" kemudian double klik folder tersebut.

3. ketikkan cmd seperti gambar berikut ini

   ![cmd2](D:\Doc_Kuliah\SEMESTER_6\cmd2.jpg)

   

4. kemudian enter maka akan muncul tampilan cmd seperti gambar berikut ini![tampil](D:\Doc_Kuliah\SEMESTER_6\tampil.jpg)



5. Pastikan laptop terhubung dengan koneksi internet, kemudian ketikkan `pip install BeautifulSoap4` lalu enter tunggu hingga proses instalasi selesai

6. Selanjutnya ketikkan `pip install requests` lalu enter dan tunggu hingga proses instalasi selesai.

7. Tahap selanjutnya yaitu membuka IDLE Python Buat File Baru dan ketikkan sourse code lengkap seperti link berikut ini :

   [source code crawler data](https://github.com/iisyuni/crawler-data-website/blob/master/source_code_crawler_data.py) 

------



## Penjelasan Program

```python
import requests
from bs4 import BeautifulSoup
import sqlite3
```

Library yang digunakan yaitu BeautifulSoup, requests dan SQLite3 untuk menyimpan data ke database

```python
src = "https://www.kompasiana.com/olahraga"
page = requests.get(src)
soup = BeautifulSoup(page.content, 'html.parser')
```

`src` adalah variabel yang digunakan untuk menampung link dari website yang akan di ambil datanya. variabel `page` digunakan untuk merequests website. sedangkan variabel `soup ` digunakan untuk mendownload semua kode html yang kemudian di ubah ke dalam objek BeautifulSoup.

```python
konten = soup.findAll(class_='timeline--artikel')
```

Setelah itu, memilih konten yang akan di ambil dalam sebuah website dengan memanggil `class_` dari konten tersebut.

```python
koneksi = sqlite3.connect('db_data.db')
koneksi.execute(''' CREATE TABLE if not exists kompasiana
            (judul TEXT NOT NULL,
             view TEXT NOT NULL,
             like TEXT NOT NULL,
             komen TEXT NOT NULL);''')
```

variabel `koneksi` digunakan untuk mengkoneksikan python dengan SQLite3 supaya bisa membuat sebuah database.

```python
for i in range(len(konten)):

    judul = konten[i].find(class_='title')
    judul = judul.find('a').getText()

    statistik = konten[i].findAll(class_='artikel--count__item')
    view=statistik[0].getText()
    like=statistik[1].getText()
    komen=statistik[2].getText()

    koneksi.execute('''INSERT INTO kompasiana values ('%s', '%s', '%s', '%s');'''%(judul, view, like, komen));

```

Setelah semua data berhasil di ambil berikutnya yaitu memasukkan data tersebut ke dalam database yang setiap program di jalan kan akan menghasilkan file baru bernama `db_data.db` file tersebut menampung data yang di ambil dari website.

```python
tampil = koneksi.execute("SELECT * FROM kompasiana")
for row in tampil:
    print(row)
```

variabel `tampil` digunakan untuk menampilkan data dari database yang sudah tersimpan. kemudian dilakukan perulangan agar semua data bisa di tampilkan.



##### Note : 

- Untuk menjalankan programnya pastikan terhubung dengan koneksi internet. Agar tidak terjadi error.
