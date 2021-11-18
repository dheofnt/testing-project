class KueCoklatManusia :
    warnaMata = 'Biru'
    warnaMulut = 'Putih'
    warnaBaju = 'Putih'
    warnaKancing = 'Merah'

kue1 = KueCoklatManusia()
kue2 = KueCoklatManusia()
kue3 = KueCoklatManusia()

print(kue1, type(kue1))
print(kue2, type(kue2))
print(kue3, type(kue3))

print(kue1.warnaMata, type(kue1.warnaMata))
print(kue2.warnaMata, type(kue2.warnaMata))
print(kue3.warnaMata, type(kue3.warnaMata))

kue2.warnaMata = 'Hitam'

print(kue1.warnaMata, type(kue1.warnaMata))
print(kue2.warnaMata, type(kue2.warnaMata))
print(kue3.warnaMata, type(kue3.warnaMata))