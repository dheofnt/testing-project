# 1

# print(not(True))
# print(not(False))

# hasil1 = not((5 > 2 or 4 == 5) and 5 != 5)
# hasil2 = not('hello' == 'hello')
# hasil3 = not(4 > 3 and 'apa' == 'Apa')
# hasil4 = not(3 > 5 or (7 != 8 and 'kari' != 'kuri'))
# hasil5 = not(5 != 5 and 7 > 2)

# print('Hasil1 =', hasil1, type(hasil1))
# print('Hasil2 =', hasil2, type(hasil2))
# print('Hasil3 =', hasil3, type(hasil3))
# print('Hasil4 =', hasil4, type(hasil4))
# print('Hasil5 =', hasil5, type(hasil5))

# ============================================================================#

# 2

# print('Selamat datang!')

# umur = int(input('Masukkan Umurmu : '))

# if(umur >= 17) :
#     print('Anda sudah boleh bikin SIM')
#     nama = input('Masukkan Namamu : ')
#     if(len(nama) > 1) :
#         print('Terima Kasih {}'.format(nama))

# print('Sampai Jumpa!')

# =============================================================================== #

# 3

# print('Selamat datang!')
# umur = int(input('Masukkan Umurmu : '))
# if(umur >= 17) :
#     print('Anda sudah boleh bikin SIM')
#     nama = input('Masukkan Namamu : ')
#     if(len(nama) >1 ) :
#         print('Terima Kasih {}'.format(nama))
#     else :
#         print('Nama harus diatas 1 huruf')
# else :
#     print('Anda belum boleh bikin SIM karena Umur harus 17 tahun atau lebih')

# print('Sampai Jumpa!')

# ================================================================================ #

# 4.

print('Pengecheckan Ujian')

nilai = int(input('Masukkan Nilai : '))
grade = ''

if(nilai >= 90 and nilai <=100) :
    grade = 'A'
elif(nilai >= 80 and nilai <= 89) :
    grade = 'B'
elif(nilai >= 70 and nilai <= 79) :
    grade = 'C'
elif(nilai >= 60 and nilai <= 69) :
    grade = 'D'
elif(nilai >= 0 and nilai <= 59) :
    grade = 'F'
else :
    grade = 'Nilai harus diinput dari jarak 0 - 100'

print('Grade = {}'.format(grade))


