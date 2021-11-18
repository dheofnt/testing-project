listBuah = [
    {
        'nama': 'Apel',
        'stok': 20,
        'harga': 10000
    },
    {
        'nama': 'Jeruk',
        'stok': 15,
        'harga': 15000
    },
    {
        'nama': 'Anggur',
        'stok': 25,
        'harga': 20000
    }
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
            print('{}\t|{}\t\t|{}\t|{}'.format(i, listBuah[i]['nama'], listBuah[i]['stok'], listBuah[i]['harga']))
    
    elif(pilihanMenu == '2') :
        namaBuah = str(input('Masukkan Nama Buah : '))
        stokBuah = int(input('Masukkan Stok Buah : '))
        hargaBuah = int(input('Masukkan Harga Buah : '))
        listBuah.append({
            'nama': namaBuah,
            'stok': stokBuah,
            'harga': hargaBuah
        })
        print('Daftar Buah\n')
        print('Index\t|Nama\t\t|Stok\t|Harga')
        for i in range(len(listBuah)) :
            print('{}\t|{}\t\t|{}\t|{}'.format(i, listBuah[i]['nama'], listBuah[i]['stok'], listBuah[i]['harga']))

    elif(pilihanMenu == '3') :
        print('Daftar Buah\n')
        print('Index\t|Nama\t\t|Stok\t|Harga')
        for i in range(len(listBuah)) :
            print('{}\t|{}\t\t|{}\t|{}'.format(i, listBuah[i]['nama'], listBuah[i]['stok'], listBuah[i]['harga']))        
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
            print('{}\t|{}\t\t|{}\t|{}'.format(i, listBuah[i]['nama'], listBuah[i]['stok'], listBuah[i]['harga']))            
    
    elif(pilihanMenu == '4') :
        print('Daftar Buah\n')
        print('Index\t|Nama\t\t|Stok\t|Harga')
        for i in range(len(listBuah)) :
            print('{}\t|{}\t\t|{}\t|{}'.format(i, listBuah[i]['nama'], listBuah[i]['stok'], listBuah[i]['harga']))            
        while True :
            indexBuah = int(input('Masukkan index buah yang ingin dibeli : '))
            qtyBuah = int(input('Masukkan Jumlah Buah yang Ingin Dibeli : '))
            if (qtyBuah > listBuah[indexBuah]['stok']) :
                print('Stok buah tidak cukup, stok {} tinggal {}'.format(listBuah[indexBuah]['nama'], listBuah[indexBuah]['stok']))
            else :
                cart.append({
                    'nama': listBuah[indexBuah]['nama'],
                    'qty': qtyBuah,
                    'harga': listBuah[indexBuah]['harga'],
                    'index': indexBuah
                })
            print('Isi Cart :')
            print('Nama\t|Qty\t|Harga')
            for item in cart :
                print('{}\t|{}\t|{}'.format(item['nama'], item['qty'], item['harga']))
            checker = input('Mau beli yang lain? (ya/tidak) = ')
            if checker == 'tidak' :
                break
        print('Daftar Belanja :')
        print('Nama\t|Qty\t|Harga\t|Total Harga')
        totalHarga = 0
        for item in cart :
            print('{}\t|{}\t|{}\t|{}'.format(item['nama'], item['qty'], item['harga'], item['qty'] * item['harga']))
            totalHarga += item['qty'] * item['harga']
        while True :
            print('Total Yang Harus Dibayar = {}'.format(totalHarga))
            jumlahUang = int(input('Masukkan Jumlah Uang : '))
            if jumlahUang > totalHarga :
                kembali = jumlahUang - totalHarga
                print('Terima Kasih \nUang Kembali Anda : {}'.format(kembali))
                for item in cart :
                    listBuah[item['index']]['stok'] -= item['qty']
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
