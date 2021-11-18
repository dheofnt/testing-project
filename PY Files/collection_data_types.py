# LIST 024  -1 -2 -5  -4:-1  1:4  -5:2  0:-2  2:   

# index = >     0/-5    1/-4    2/-3    3/-2    4/-1
listContoh = ['hello',    1,      1,      3,    True]

print(listContoh, type(listContoh))

print(listContoh[0])
print(listContoh[2])
print(listContoh[4])

print(listContoh[-1])
print(listContoh[-2])
print(listContoh[-5])

print(listContoh[-4:1])
print(listContoh[1:4])
print(listContoh[-5:2])
print(listContoh[0:-2])
print(listContoh[2:])


# MENGGANTI ISI VARIABEL DI LIST

# index = >     0/-5    1/-4    2/-3    3/-2    4/-1
listContoh = ['hello',    1,      1,      3,    True]
listContoh[2] = 'Dheo'
print(listContoh)

# APPEND & INSERT
# index = >     0/-5    1/-4    2/-3    3/-2    4/-1
listContoh = ['hello',    1,      1,      3,    True]

listContoh.append('coba')
listContoh.insert(1, 'boleh')

print(listContoh) # ['hello', 'boleh', 1, 1, 3, True, 'coba']



# MENGHAPUS VARIABLE DALAM LIST
# index = >     0/-5    1/-4    2/-3    3/-2    4/-1
listContoh = ['hello', 'coba', 'coba',   3,    True]

listContoh.remove('coba')
listContoh.pop()
del listContoh[1]
print(listContoh)

listContoh.clear()
print(listContoh)

# LOOP DALAM LIST
# FOR
# index = >     0/-5    1/-4    2/-3    3/-2    4/-1
listContoh = ['hello',    1,      1,      3,    True]

for item in listContoh :
    print(item)


# CHECK IF AN ITEM IS IN A LIST
# index = >     0/-5    1/-4    2/-3    3/-2    4/-1
listContoh = ['hello',    1,      1,      3,    True]

check = 2 in listContoh
print(check)

if 'hello' in listContoh :
    print('Ada string hello di listContoh')
else :
    print('Tidak ada string hello di listContoh')

# COPY OF LIST

# index = >     0/-5    1/-4    2/-3    3/-2    4/-1
listContoh = ['hello', 'coba', 'coba',   3,    True]

newList1 = listContoh
newList1[1] = 'test'

newList2 = listContoh.copy()
newList2[2] = 'baru'


# List campur list

# index = >     0/-5    1/-4    2/-3    3/-2    4/-1
listContoh = ['hello', 'coba', 'coba',   3,    True]
listBaru = [5, 'test', False]
listCoba = ['tarik', 8]

listGabungan = listBaru + listContoh
print(listGabungan)  ## => hasil  [5, 'test', False, 'hello', 'coba', 'coba', 3, True]

listGabungan.extend(listCoba)
print(listGabungan)  ## => hasil  [5, 'test', False, 'hello', 'coba', 'coba', 3, True, 'tarik', 8]

# FIND INDEX
# index = >     0/-5    1/-4    2/-3    3/-2    4/-1
listContoh = ['eddie', 'baron', 'andi', 'charlie', 'samson']
indexYgDicari1 = listContoh.index('andi')
print(indexYgDicari1)

indexYgDicari2 = listContoh.index('dheo')
print(indexYgDicari2)

# SORTING ASC
# index = >     0/-5    1/-4    2/-3    3/-2    4/-1
listContoh = ['eddie', 'baron', 'andi', 'charlie', 'samson']
listContoh.sort()
print(listContoh) ##> hasil nya ['andi', 'baron', charlie, 'eddie, 'samson']


# SORTING puter balik
# index = >     0/-5    1/-4    2/-3    3/-2    4/-1
listContoh = ['eddie', 'baron', 'andi', 'charlie', 'samson']
listContoh.reverse()
print(listContoh) ##> hasil nya ['samson', 'charlie', 'andi', 'baron', 'eddie']


listAngka = [4, 3, 1, 5, 2]
listContoh.sort(reverse=True)
print(listAngka)

# LIST DALAM LIST
things = [
    ['red pen', 'blue pen'],
    ['analog clock', 'digital clock'],
    ['futsal shoes', 'badminton shoes']
]

print(things)
print(things[2])
print(things[1]) # ['analog clock', 'digital clock']
print(things[1][1]) # digital clock
print(things[2][0]) # futsal shoes
print(things[0][1]) # blue pen

# contoh lg

contoh = [
    [
        ['hello', 'apa', 'kabar'],
        [1, 2 ,3]
    ],
    [
        [True, False, [1, [2, 3]]]
    ]
]

print(contoh)
print(contoh[0][1][1])
print(contoh[1][0][2][1][1])


# TUPLE = LIST
# =================================================================================================================================================
# DICTIONARY
# CARA 1
dictionaryContoh1 = {
    'nama' : 'Budi',
    'usia' : '25',
    'pekerjaan' : 'Developer'
}

# CARA 2
dictionaryContoh2 = dict(nama='Andi', usia=27, pekerjaan='Data Scientist')

print(dictionaryContoh1['nama'])
print(dictionaryContoh1.get('nama'))

# TAMBAH KEY DAN VARIABLE
dictionaryContoh1['kelamin'] = 'Pria'

#==============================================================================================
#SET


