hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000
stokApel = 5
stokJeruk = 7
stokAnggur = 6

print('Selamat datang di Toko Dheo')

while (True) :
    jumlahApel = int(input('Masukkan jumlah Apel : '))
    if (jumlahApel > stokApel) :
        print('Jumlah yang dimasukkan terlalu banyak \nStok Apel tinggal : {}'.format(stokApel))
    else :
        break

while (True):
    jumlahJeruk = int(input('Masukkan jumlah Jeruk : '))
    if (jumlahJeruk > stokJeruk) :
        print('Jumlah yang dimasukkan terlalu banyak \nStok Jeruk tinggal : {}'.format(stokJeruk))
    else :
        break

while (True):
    jumlahAnggur = int(input('Masukkan jumlah Anggur : '))
    if (jumlahAnggur > stokAnggur) :
        print('Jumlah yang dimasukkan terlalu banyak \nStok Anggur tinggal : {}'.format(stokAnggur))
    else :
        break

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


while(True) :
    uang = (int(input('Masukkan jumlah uang : ')))

    if(uang > ttlHarga) :
        print('Transaksi berhasil,\nUang kembalian anda : {}'.format(uang - ttlHarga))
        break
    elif(uang == ttlHarga) :
        print('Transaksi berhasil, Terima Kasih!')
        break
    else :
        print('Transaksi dibatalkan \nUang anda kurang sebesar : {}'.format(ttlHarga - uang))
