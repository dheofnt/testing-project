hari = {
    "senin" : "monday",
    "selasa" : "tuesday",
    "rabu" : "wednesday",
    "kamis" : "thursday",
    "jumat" : "friday",
    "sabtu" : "saturday",
    "minggu" : "sunday"
}

try :
    inputHari = str.lower(input('Masukkan Nama Hari : '))
    if inputHari == 'monday':
        print('Hari yang anda pilih {} dalam bahasa Indonesia adalah senin'.format(inputHari))
    elif inputHari == 'senin' :
        print('Hari yang anda pilih {} dalam bahasa Inggris adalah {}'.format(inputHari, hari["senin"]))
    elif inputHari == 'tuesday' :
        print('Hari yang anda pilih {} dalam bahasa Indonesia adalah selasa'.format(inputHari))
    elif inputHari == 'selasa' :
        print('Hari yang anda pilih {} dalam bahasa Inggris adalah {}'.format(inputHari, hari["selasa"]))
    elif inputHari == 'wednesday' :
        print('Hari yang anda pilih {} dalam bahasa Indonesia adalah rabu'.format(inputHari))
    elif inputHari == 'rabu' :
        print('Hari yang anda pilih {} dalam bahasa Inggris adalah {}'.format(inputHari, hari["rabu"]))
    elif inputHari == 'thursday' :
        print('Hari yang anda pilih {} dalam bahasa Indonesia adalah kamis'.format(inputHari))
    elif inputHari == 'kamis' :
        print('Hari yang anda pilih {} dalam bahasa Inggris adalah {}'.format(inputHari, hari["kamis"]))
    elif inputHari == 'friday' :
        print('Hari yang anda pilih {} dalam bahasa Indonesia adalah jumat'.format(inputHari))
    elif inputHari == 'jumat' :
        print('Hari yang anda pilih {} dalam bahasa Inggris adalah {}'.format(inputHari, hari["jumat"]))
    elif inputHari == 'saturday' :
        print('Hari yang anda pilih {} dalam bahasa Indonesia adalah sabtu'.format(inputHari))
    elif inputHari == 'sabtu' :
        print('Hari yang anda pilih {} dalam bahasa Inggris adalah {}'.format(inputHari, hari["sabtu"]))
    elif inputHari == 'sunday' :
        print('Hari yang anda pilih {} dalam bahasa Indonesia adalah minggu'.format(inputHari))
    elif inputHari == 'minggu' :
        print('Hari yang anda pilih {} dalam bahasa Inggris adalah {}'.format(inputHari, hari["minggu"]))
    elif inputHari == " "  or inputHari == "" :
        print('nama hari yang anda masukan tidak ada')
    else :
        print('Nama hari yang anda masukkan salah')
except :
    print('ashiap')

# print(fruit.get('kiwi'))
# 2.0
