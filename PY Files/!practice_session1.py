# SOAL 1

# Jumlah Hewan 13
# Jumlah seluruh kaki hewan 32
# Ada ayam dan kambing
# x + y = 13
# 2x + 4y = 32
# 2x + 4(13 - x) = 32
# 2x - 4x + (4 * 13) = 32
# 2x - 4x = 32 - (4 * 13)
# x (2 - 4) = 32 - (4 * 13)
# x = (32 - (4 * 13)) / (2 - 4)

x = 'ayam'
y = 'kambing'
kakiAyam = 2
kakiKambing = 4
jumlahHewan = 13
jumlahKakiHewan = 32

jumlahAyam = (jumlahKakiHewan - (kakiKambing * jumlahHewan)) / (kakiAyam - kakiKambing)
jumlahKambing = jumlahHewan - jumlahAyam
print('Jumlah Ayam ada {}, dan jumlah Kambing ada {}'.format(jumlahAyam, jumlahKambing))


#==============================================================================================

# SOAL 2 

# SEMBILAN BELAS TAHUN YG LALU, UMUR ANAK SETENGAH TAHUN LEBIH MUDA DARI SEPEREMPAT UMUR
# IBUNYA. UMUR ANAK SEKARANG, SEMIBLAN BELAS TAHUN LEBIH TUA DARI SEPERTUJUH UMUR IBUNYA.
# BERAPA UMUR IBU KETIKA MELAHIRKAN ANAKNYA
# OUTPUT UMUR IBU KETIKA MELAHIRKAN ANAKANYA ADALAH ...... TAHUN

# x - 19 = 1/4 * (y - 19) - 1/2
# x = 19 + (1/7 * y)
# umur anak sekarang = x
# umur ibu sekarang = y

tahun = 19
selisih = 1/2
ibu1 = 1/4
ibu2 = 1/7

# 1/7y + 19 - 19 = 1/4 * (y - 19) - 1/2
# 1/7y = 1/4 * (y - 19) - 1/2
# 1/7y = 1/4y - (1/4 * 19) - 1/2
# 1/7y - 1/4y = - (1/4 * 19) - 1/2
# (1/7 - 1/4) y = - (1/4 * 19) - 1/2
# y = (- (1/4 * 19) - 1/2) / (1/7 - 1/4)

umurIbuSekarang = round((-(ibu1 * tahun) - selisih) / (ibu2 - ibu1))
umurAnakSekarang = tahun + (ibu2 * umurIbuSekarang)
umurIbuMelahirkan = umurIbuSekarang - umurAnakSekarang
print('Umur ibu ketika melahirkan anaknya adalah {} tahun'.format(umurIbuMelahirkan))



#==============================================================================================

# SOAL 3

# JUMLAH USIA BUDI DAN AYAHNYA SEKARANG ADALAH 50 TAHUN
# EMPAT TAHUN LALU USIA AYAH ENAM KALI USIA BUDI
# BERAPA USIA BUDI DAN AYAHNYA SAAT INI
# OUTPUT USIA AYAH SAAT INI ADALAH ... TAHUN DAN USIA BUDI SAAT INI ADALAH ... TAHUN

# usia budi = x
# usia ayah = y
# USIA BUDI + AYAH = 50
# USIA BUDI 4 TAHUN LALU + AYAH 4 TAHUN LALU = 42
# x + y = 50
jumlahUmur = 50
jumlahUmur4 = 42
tahun3 = 4
selisih3 = 6
rasio4 = 1/6
rasioAyah4 = 6
rasioBudi4 = 1
rasioTotal = 7

umurBudi4 = jumlahUmur4 * (rasioBudi4 / rasioTotal)
umurAyah4 = jumlahUmur4 * (rasioAyah4 / rasioTotal)
umurBudi = umurBudi4 + 4
umurAyah = umurAyah4 + 4

print('Usia Ayah saat ini adalah {} tahun dan usia Budi saat ini adalah {} tahun'.format(umurAyah, umurBudi))


# 4 - y = 6 * x   =====># JUMLAH USIA BUDI DAN AYAHNYA SEKARANG ADALAH 50 TAHUN dan EMPAT TAHUN LALU USIA AYAH ENAM KALI USIA BUDI

# y = (6 * x) + 4
# y = (6 * (50 - y)) + 4
# y = (6 * 50) - (6y) + 4
# y + 6y = (6 * 50) + 4
# y = (6 * 50) + 4 / (1 + 6)
   
# y = (-6y + (6*50)) - 4
# y + 6y = (6*50) - 4
# y (1 + 6) = (6*50) - 4
# y = ((6*50) - 4) / (1 + 6)




#==============================================================================================

