# i = 0
# while (i < 5) :
#     print('Angka {}'.format(i))
#     i += 1

# FUNCTION RANGE
# CONTOH 1
# print('Contoh 1 : ')
# data1 = range(5)
# print(data1, type(data1))

# listData1 = list(data1)
# print(listData1, type(listData1), '\n')

# # CONTOH 2 
# print('Contoh 2 : ')
# data2 = range(5, 9)
# print(data2, type(data2))

# listData2 = list(data2)
# print(listData2, type(listData2), '\n')

# # CONTOH 3
# print('Contoh 3 :')
# data3 = range(7, 3)
# print(data3, type(data3))

# listData3 = list(data3)
# print(listData3, type(listData3), '\n')

# # CONTOH 4
# print('Contoh 4 :')
# data4 = range(7, 3, -1)
# print(data4, type(data4))

# listData4 = list(data4)
# print(listData4, type(listData4), '\n')

# # CONTOH 5
# print('Contoh 5: ')
# data5 = range(2, 14, 3)
# print(data5, type(data5))

# listData5 = list(data5)
# print(listData5, type(listData5), '\n')

# ============================================================================================================================================================================================

# FOR LOOP

# CONTOH 1

# from typing import Text


# for angka in range(5) :
#     print(angka)

# # CONTOH 2 

# for angka in range(10, 2, -3) :
#     print('Angka = {}'.format(angka))

# # contoh 3

# for char in 'Hello Guys!' :
#     print('char = ', char)

# ===============================================================================================================================================================================

# break and continue

## break ##
# contoh 1

jmlPutaran = 0
while(True) :
    jmlPutaran += 1
    print('Putaran {}'.format(jmlPutaran))

    inputan = input('Masukkan yes untuk keluar : ')
    if(inputan == 'yes') :
        break

# # contoh 2

text = 'Dheo Farhan Nugraha Tambunan'
hurufYgDicari = input('Masukkan huruf yang ingin dicari pada text ({}) : '.format(text))
index = 0

for c in text :
    if (c == hurufYgDicari) :
        break

    index += 1

if(index == len(text)) :
    print('Huruf {} tidak ditemukan'.format(hurufYgDicari))
else :
    print('Huruf {} pertama ditemukan pada indek ke {}'.format(hurufYgDicari, index))


# ## continue ## 
text = 'Halo apa kabar?'
hurufYgInginDilewati = input('Masukkan huruf yang ingin dilewati : ')

for c in text :
    if (c == hurufYgInginDilewati) :
        continue
    print(c)

# ===========================================================================================================================================================

# LOOP DRAWING

# horizontal
stars = ''

for i in range(5) :
    stars += '* '

print(stars)

# ============
# vertical
stars = ''

for i in range(5) :
    stars += '* \n'

print(stars)

# =============

# persegi
stars = ''
size = 5

for i in range(size) :
    for j in range(size) :
        stars += '* '
    stars += '\n'

print(stars)

# =============

# segitiga siku rata kiri
stars = ''
size = 5

for i in range(size) :
    for j in range(i + 1) :
        stars += '* '
    stars += '\n'

print(stars)

# HASIL
# *
# * *
# * * *
# * * * *
# * * * * *

