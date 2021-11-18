# Masukkan jumlah uang : 135000
# Transaksi anda dibatalkan
# uangnya kurang sebesar 25000

# Masukkan jumlah uang : 160000
# Transaksi berhasil, Terima kasih!

# Masukkan jumlah uang : 175000
# Transaksi berhasil
# Uang kembali anda : 15000
# Terima kasih!

hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

print('Selamat datang di Toko Dheo')

jumlahApel = int(input('Masukkan jumlah Apel : '))
jumlahJeruk = int(input('Masukkan jumlah Jeruk : '))
jumlahAnggur = int(input('Masukkan jumlah Anggur : '))

totalHargaApel = jumlahApel * hargaApel
totalHargaJeruk = jumlahJeruk * hargaJeruk
totalHargaAnggur = jumlahAnggur * hargaAnggur
ttlHarga = totalHargaApel + totalHargaJeruk + totalHargaAnggur

print('''
Detail Belanja

Apel : {jmlApel} x {hrgApel} = {totalHrgApel}
Jeruk : {jmlJeruk} x {hrgJeruk} = {totalHrgJeruk}
Anggur : {jmlAnggur} x  {hrgAnggur} = {totalHrgAnggur}

Total : {totalHarga}
'''.format(jmlApel=jumlahApel, hrgApel=hargaApel, totalHrgApel=totalHargaApel,
    jmlJeruk=jumlahJeruk, hrgJeruk=hargaJeruk, totalHrgJeruk=totalHargaJeruk,
    jmlAnggur=jumlahAnggur, hrgAnggur=hargaAnggur, totalHrgAnggur=totalHargaAnggur,
    totalHarga=totalHargaApel + totalHargaJeruk + totalHargaAnggur))

uang = (int(input('Masukkan jumlah uang : ')))
if(uang == ttlHarga) :
    print('Transaksi Berhasil, Terima Kasih!')
elif(uang > ttlHarga) :
    print('Terima kasih, Uang Kembali anda : {}'.format(uang - ttlHarga))
else :
    print('Transaksi anda dibatakkan')
    print('Uangnya kurang sebesar {}'.format(ttlHarga - uang))
