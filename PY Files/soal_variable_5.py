# jarak mobil a & b = 120 km
# A berjalan 60km/h dari timur
# B berjalan 40km/h dari barat
# A & B start pukul 9 WIB
# Jam berapa A & B bertabrakan?

# 60 km/h + 40 km/h = 100 km/h
# dengan kecepatan 100 km/h. Berapa waktu yang dibutuhkan untuk menempuh jarak 120 km?
# 120 / 100 = 1.2 jam
# 1.2 * 60 = 72 menit => 60 menit + 12 menit
# start jam 9:00 dan akan bertemu pada jam 10:12

import math

jamAwal = 9
jarakKM = 120
kecepatanTotalKMperJam = 100
kecepatanTotalKMperDetik = kecepatanTotalKMperJam / 3600

detikTotal = jarakKM / kecepatanTotalKMperDetik
lamaJam = math.floor(detikTotal / 3600)
lamaMenit = math.floor(detikTotal % 3600 / 60)
lamaDetik = math.floor(detikTotal % 3600 % 60)

print('Tabraknya pukul {}:{}:{}0'.format(jamAwal + lamaJam,lamaMenit,lamaDetik))


