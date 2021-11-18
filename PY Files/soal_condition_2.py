# imt = massa(KG) / tinggi(METER) ^ 2
# imt < 18.5 artinya berat badan kurang,
# 18.5 - 24.9 artinya berat badan ideal,
# 25.0 - 29.9 artinya berat badan berlebih,
# 30.0 - 39.9 artinya berat badan sangat berlebih,
# imt > 39.9 artinya obesitas

print('Halo, Selamat Datang!')
print('Kami bisa menghitung berat badan kamu termasuk ideal atau tidak,')
print('caranya cukup mudah, cukup masukan Berat Badan dan juga Tinggi Badan di bawah ini!')

bb = int(input('Masukkan Berat Badan Mu (kg) : '))
tb = int(input('Masukkan Tinggi Badan mu (cm) : '))
tbm = tb / 100
print('Massa {} kg dan tinggi {} m'.format(bb, tbm))

import math

imt = (bb / tbm ** 2)
if(imt < 18.5) :
    print('IMT = {}, BERAT BADAN KURANG!'.format(imt))
elif(imt >= 18.5 and imt <= 24.9) :
    print('IMT = {}, BERAT BADAN IDEAL!'.format(imt))
elif(imt >= 25.0 and imt <= 29.9) :
    print('IMT = {}, BERAT BADAN BERLEBIH!'.format(imt))
elif(imt >= 30.0 and imt <= 39.9) :
    print('IMT = {}, BERAT BADAN SANGAT BERLEBIH'.format(imt))
elif(imt > 39.9) :
    print('IMT = {}, OBESITAS!'.format(imt))