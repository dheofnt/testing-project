listBuah = [
    ['Apel', 20, 10000],
    ['Jeruk', 15, 15000],
    ['Anggur', 25, 20000]
]

cart = []

while True :
    pilihanMenu = input('''
    Selamat Datang di Pasar Buah

    List Menu :
    1. Menampilkan Daftar Buah
    2. Menambahkan Buah
    3. Menghapus Buah
    4. Membeli Buah
    5. Exit Program

    Masukkan angka Menu yang ingin dijalankan :  ''')

    if(pilihanMenu == '1') :
        print('Daftar Buah\n')
        print('Index\t|Nama\t\t|Stok\t|Harga')
        for i in range(len(listBuah)) :
            print('{}\t|{}\t\t|{}\t|{}'.format(i, listBuah[i][0], listBuah[i][1], listBuah[i][2]))
    
    elif(pilihanMenu == '2') :
        namaBuah = str(input('Masukkan Nama Buah : '))
        stokBuah = int(input('Masukkan Stok Buah : '))
        hargaBuah = int(input('Masukkan Harga Buah : '))
        listBuah.append([namaBuah,stokBuah,hargaBuah])
        print('Daftar Buah\n')
        print('Index\t|Nama\t\t|Stok\t|Harga')
        for i in range(len(listBuah)) :
            print('{}\t|{}\t\t|{}\t|{}'.format(i, listBuah[i][0], listBuah[i][1], listBuah[i][2]))

    elif(pilihanMenu == '3') :
        print('Daftar Buah\n')
        print('Index\t|Nama\t\t|Stok\t|Harga')
        for i in range(len(listBuah)) :
            print('{}\t|{}\t\t|{}\t|{}'.format(i, listBuah[i][0], listBuah[i][1], listBuah[i][2]))        
        buahApus = str(input('Masukkan Nama Buah yang Ingin Dihapus : '))
        if buahApus == 'Apel' :
            del listBuah[0]
        elif buahApus == 'Jeruk' :
            del listBuah[1]
        elif buahApus == 'Anggur' :
            del listBuah[2]
        print('Daftar Buah\n')
        print('Index\t|Nama\t\t|Stok\t|Harga')
        for i in range(len(listBuah)) :
            print('{}\t|{}\t\t|{}\t|{}'.format(i, listBuah[i][0], listBuah[i][1], listBuah[i][2]))            
    
    elif(pilihanMenu == '4') :
        print('Daftar Buah\n')
        print('Index\t|Nama\t\t|Stok\t|Harga')
        for i in range(len(listBuah)) :
            print('{}\t|{}\t\t|{}\t|{}'.format(i, listBuah[i][0], listBuah[i][1], listBuah[i][2]))            
        while True :
            indexBuah = int(input('Masukkan index buah yang ingin dibeli : '))
            qtyBuah = int(input('Masukkan Jumlah Buah yang Ingin Dibeli : '))
            if (qtyBuah > listBuah[indexBuah][1]) :
                print('Stok buah tidak cukup, stok {} tinggal {}'.format(listBuah[indexBuah][0], listBuah[indexBuah][1]))
            else :
                cart.append([listBuah[indexBuah][0], qtyBuah, listBuah[indexBuah][2], indexBuah])
            print('Isi Cart :')
            print('Nama\t|Qty\t|Harga')
            for item in cart :
                print('{}\t|{}\t|{}'.format(item[0], item[1], item[2]))
            checker = input('Mau beli yang lain? (ya/tidak) : ')
            if checker == 'tidak' :
                break
        print('Daftar Belanja :')
        print('Nama\t|Qty\t|Harga\t|Total Harga')
        totalHarga = 0
        for item in cart :
            print('{}\t|{}\t|{}\t|{}'.format(item[0], item[1], item[2], item[1] * item[2]))
            totalHarga += item[1] * item[2]
        while True :
            print('Total Yang Harus Dibayar = {}'.format(totalHarga))
            jumlahUang = int(input('Masukkan Jumlah Uang : '))
            if jumlahUang > totalHarga :
                kembali = jumlahUang - totalHarga
                print('Terima Kasih \nUang Kembali Anda : {}'.format(kembali))
                for item in cart :
                    listBuah[item[3]][1] -= item[1]
                cart.clear()
                break
            elif jumlahUang == totalHarga :
                print('Terima Kasih')
                break
            else :
                kekurangan = jumlahUang - totalHarga
                print('Uang anda kurang sebesar {}'.format(kekurangan))
    elif(pilihanMenu == '5'):
        break
    break