#1 tahun 365 hari
#1 bulan 30 hari
#1 minggu 7 hari

import math

try :
    inputHari = int(input('Masukkan Jumlah Hari : '))
    sisaHari = inputHari

    tahun = math.floor(inputHari / 365)
    sisaHari %= 365
    bulan = math.floor(sisaHari / 30)
    sisaHari %= 30
    minggu = math.floor(sisaHari / 7)
    sisaHari %= 7

    if inputHari >= 0 and inputHari < 4000 :
        print('{} Tahun {} Bulan {} Minggu {} Hari'.format(tahun, bulan, minggu, sisaHari))
    if inputHari > 4000 :
        print('Jumlah Hari diatas batas')
    elif inputHari < 0 :
        print('Jumlah Hari dibawah batas')
except :
    print('Tidak menerima text atau desimal')