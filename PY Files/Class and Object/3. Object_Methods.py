class KueCoklatManusia:
    def __init__(self, eyeColor, buttonsColor) :
        print('1 kue sedang dibuat')
        self.warnaMata = eyeColor
        self.warnaMulut = 'Putih'
        self.warnaBaju = 'Putih'
        self.warnaKancing = buttonsColor
    
    def infoWarnaKue(self, nama='Unknown') :
        print('''
        Info Warna Kue untuk {}:
        
        Warna Mata = {}
        Warna Mulut = {}
        Warna Baju {}
        Warna Kancing {}
        '''.format(nama, self.warnaMata, self.warnaMulut, self.warnaBaju, self.warnaKancing))

kue1 = KueCoklatManusia('Biru', 'Merah')
kue2 = KueCoklatManusia(eyeColor='Hitam', buttonsColor = 'Merah')
kue3 = KueCoklatManusia(buttonsColor = 'Coklat', eyeColor='Green')
    
    
kue1.infoWarnaKue()
kue2.infoWarnaKue('Andi')
kue3.infoWarnaKue(nama='Budi')