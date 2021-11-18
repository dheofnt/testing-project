import math
# 485 Hari = 1 Tahun, 4 Bulan, 0 Minggu, 5 Hari

# tahun = 1
# bulan = 4
# minggu = 0
# hari = 5
# hasil = "{jmlTahun} tahun, {jmlBulan} bulan, {jmlMinggu} minggu, {jmlHari} hari."
# print(hasil.format(jmlTahun=tahun, jmlBulan=bulan, jmlMinggu=minggu, jmlHari=hari))


# hasil2 = "{} tahun, {} bulan, {} minggu, {} hari."
# hasil2 = hasil2.format(tahun, bulan, minggu, hari)
# print(hasil2)


jmlHari = 485
sisaHari = jmlHari

# 485 / 360 = 1.1201031 => dibulatkan menjadi 1
# variabel tahun menjadi int 1
tahun = math.floor(jmlHari/360)

# 485 % 360 = 125
# sisa hari 125
sisaHari %= 360

# 125 / 30 = 4.5 => dibulatkan menjadi 4
# variabel bulan menjadi int 4
bulan = math.floor(sisaHari/30)

# 125 % 30 = 5
# sisa hari 5
sisaHari %= 30

# 5 / 7 = 0.78 => dibulatkan kebawah menjadi 0
# variabel minggu menjadi int 0
minggu = math.floor(sisaHari/7)

# 5 % 7 = 5
# sisa hari menjadi int 5
sisaHari %= 7

print(str(jmlHari) + " hari adalah")
print('{} tahun'.format(tahun))
print('{} bulan'.format(bulan))
print('{} minggu'.format(minggu))
print('{} hari'.format(sisaHari))
