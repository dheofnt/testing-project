hari = {
    "senin" : "monday",
    "selasa" : "tuesday",
    "rabu" : "wednesday",
    "kamis" : "thursday",
    "jumat" : "friday",
    "sabtu" : "saturday",
    "minggu" : "sunday"
}

inputHari = str.lower(input('Masukkan hari : '))
if not inputHari:
    print('Nama Hari yang anda masukkan salah')

while False :
    break

while True :
    for key,value in hari.items():
        if value == 'monday' and inputHari == 'monday':
            print('Hari yang anda pilih {} dalam bahasa Indonesia adalah senin'.format(inputHari))
        elif key == 'senin' and inputHari == 'senin' :
            print('Hari yang anda pilih {} dalam bahasa Inggris adalah {}'.format(inputHari, hari["senin"]))
        elif value == 'tuesday' and inputHari == 'tuesday' :
            print('Hari yang anda pilih {} dalam bahasa Indonesia adalah selasa'.format(inputHari))
        elif key == 'selasa' and inputHari == 'selasa' :
            print('Hari yang anda pilih {} dalam bahasa Inggris adalah {}'.format(inputHari, hari["selasa"]))
        elif value == 'wednesday' and inputHari == 'wednesday' :
            print('Hari yang anda pilih {} dalam bahasa Indonesia adalah rabu'.format(inputHari))
        elif key == 'rabu' and inputHari == 'rabu' :
            print('Hari yang anda pilih {} dalam bahasa Inggris adalah {}'.format(inputHari, hari["rabu"]))
        elif value == 'thursday' and inputHari == 'thursday' :
            print('Hari yang anda pilih {} dalam bahasa Indonesia adalah kamis'.format(inputHari))
        elif key == 'kamis' and inputHari == 'kamis' :
            print('Hari yang anda pilih {} dalam bahasa Inggris adalah {}'.format(inputHari, hari["kamis"]))
        elif value == 'friday' and inputHari == 'friday' :
            print('Hari yang anda pilih {} dalam bahasa Indonesia adalah jumat'.format(inputHari))
        elif key == 'jumat' and inputHari == 'jumat' :
            print('Hari yang anda pilih {} dalam bahasa Inggris adalah {}'.format(inputHari, hari["jumat"]))
        elif value == 'saturday' and inputHari == 'saturday' :
            print('Hari yang anda pilih {} dalam bahasa Indonesia adalah sabtu'.format(inputHari))
        elif key == 'sabtu' and inputHari == 'sabtu' :
            print('Hari yang anda pilih {} dalam bahasa Inggris adalah {}'.format(inputHari, hari["sabtu"]))
        elif value == 'sunday' and inputHari == 'sunday' :
            print('Hari yang anda pilih {} dalam bahasa Indonesia adalah minggu'.format(inputHari))
        elif key == 'minggu' and inputHari == 'minggu' :
            print('Hari yang anda pilih {} dalam bahasa Inggris adalah {}'.format(inputHari, hari["minggu"]))
        else :
            print('Nama hari yang anda masukkan tidak ada')
    break
