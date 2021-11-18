import mysql.connector
# print("installed")

myDB = {
'user' : "DB_Admin",
'password' : 'DBAdmin99;',
'database' : 'Seller',
'host' : 'localhost'
}

conn = mysql.connector.connect(**myDB)
# print('koneksi sukses')


# INPUT VAL 
# ALT 1
Cr = conn.cursor()
# query = "INSERT INTO Aset VALUES(30, 'Lemari', 60, 850000)"

# Cr.execute(query)
# conn.commit()
# print('Data Submitted')


# ALT 2
# sql = "INSERT INTO Aset VALUES (%s, %s, %s, %s)"
# val = (21, 'Kursi', 29, 750000)
# Cr.execute(sql, val)
# conn.commit()
# print('Data Submitted')

# ID = int(input("Masukkan ID Aset : "))
# Nama = input("Masukkan Nama Aset : ")
# Stok = int(input("Masukkan Jumlah Stok : "))
# Harga = float(input("Masukkan Harga Aset : "))

# sql = "INSERT INTO Aset VALUES (%s, %s, %s, %s)"
# val = (ID, Nama, Stok, Harga)
# Cr.execute(sql, val)
# conn.commit()
# print('Data Submitted')


### UPDATE TABEL

# query = "UPDATE Aset SET Stok = 150 WHERE ID_Aset = 10"
# Cr.execute(query)
# conn.commit()
# print('Data Updated')

# Id = int(input('Masukkan ID Aset yang akan di Update : '))
# Stok = int(input('Masukkan Stok Terbaru : '))

# query = f"UPDATE Aset SET Stok = {Stok} WHERE ID_Aset = {Id}"
# Cr.execute(query)
# conn.commit()
# print('Stock Updated')


query = "SELECT * FROM Aset"
Cr.execute(query)
# hasil = Cr.fetchcall()
# for i in hasil :
#     print(i)

for i in Cr:
    print(i)
    




