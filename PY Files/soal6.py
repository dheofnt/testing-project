try :
    nilai = int and float(input('Masukkan Nilai : '))
    if(nilai >= 90 and nilai <=100) :
        grade = 'A'
        print('Nilai anda {} dan anda Grade {}'.format(nilai, grade))
    elif(nilai >= 85 and nilai <= 89) :
        grade = 'A-'
        print('Nilai anda {} dan grade anda {}'.format(nilai, grade))
    elif(nilai >= 80 and nilai <= 84) :
        grade = 'B'
        print('Nilai anda {} dan grade anda {}'.format(nilai, grade))
    elif(nilai >= 75 and nilai <= 79) :
        grade = 'B-'
        print('Nilai anda {} dan grade anda {}'.format(nilai, grade))
    elif(nilai >= 70 and nilai <= 74) :
        grade = 'C'
        print('Nilai anda {} dan grade anda {}'.format(nilai, grade))
    elif(nilai >= 65 and nilai < 70) :
        grade = 'D'
        print('Nilai anda {} dan grade anda {}'.format(nilai, grade))
    elif(nilai >= 40 and nilai <= 64) :
        grade = 'Perlu Remedial'
        print('Nilai anda {} dan grade anda {}'.format(nilai, grade))
    elif(nilai >= 0 and nilai <= 39) :
        grade = 'Tidak Lulus'
        print('Nilai anda {} dan grade anda {}'.format(nilai, grade))
    elif(nilai > 100) :
        print('Nilai diluar jangakuan')
    elif(nilai < 0) :
        print('Nilai tidak menerima angka negatif')
except :
    print('Nilai yang harus diinput harus berupa ANGKA')

