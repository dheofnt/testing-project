class KueCoklatManusia :
    def __init__(self, eyeColor, buttonsColor) :
        print('1 kue sedang dibuat')
        self.warnaMata = eyeColor
        self.warnaMulut = 'Putih'
        self.warnaBaju = 'Putih'
        self.warnaKancing = buttonsColor

kue1 = KueCoklatManusia('Biru', 'Merah')
kue2 = KueCoklatManusia(eyeColor = 'Hitam', buttonsColor = 'Merah')
kue3 = KueCoklatManusia(buttonsColor = 'Coklat', eyeColor = 'Green')

print(kue1, type(kue1))
print(kue2, type(kue2))
print(kue3, type(kue3))

print(kue1.__dict__, type(kue1.__dict__))
print(kue2.__dict__, type(kue2.__dict__))
print(kue3.__dict__, type(kue3.__dict__))
