# saat ini, jumlah Usia Andi & Budi = 49 th,
# dengan ratio Usia Andi & Budi = 0.4.
# 0.4 = 4 / 10=> 4 : 10 => 2 : 5
# total ratio => 2 + 5 = 7
# usiaAndi = total umur * (ratio Andi / ratio Total)
# usiaBudi = total umur * (ratio Budi / ratio total)

totalUmur = 49
ratioAndi = 2
ratioBudi = 5
ratioTotal = 7

usiaAndi = totalUmur * (ratioAndi / ratioTotal)
usiaBudi = totalUmur * (ratioBudi / ratioTotal)

print('Usia Andi sekarang adalah {}'.format((int(usiaAndi))))
print('Usia Budi sekarang = {}'.format(usiaBudi))

print('Usia Andi dua tahun lagi adalah {}'.format(int(usiaAndi) + 2))
print('Usia Budi dua tahun lagi adalah {}'.format(int(usiaBudi) + 2))

