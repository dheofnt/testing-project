# BMI = massa(KG) / tinggi(METER) ^ 2
# bmi1 = BMI < 18.5 artinya berat badan kurang,
# bmi2 = 218.5 - 24.9 artinya berat badan ideal,
# bmi3 = 25.0 - 29.9 artinya berat badan berlebih,
# bmi4 = 30.0 - 39.9 artinya berat badan sangat berlebih,
# bmi5 = BMI > 40 artinya obesitas

try :
    bb = int(input('Masukkan Berat Badan Mu (kg) : '))
    if bb > 250 :
        print('Berat badan diatas batas')
    elif bb < 0 :
        print('Tidak menerima angka negatif')
    tb = int(input('Masukkan Tinggi Badan mu (cm) : '))
    if tb > 300 :
        print('Tinggi badan diatas batas')
    elif tb < 0 :
        print('Tidak menerima angka negatif')

    print('Massa {} kg dan tinggi {} m'.format(bb, tb/100))
    import math
    bmi = round((bb / (tb / 100) ** 2),2)
    if(bmi >= 0 and bmi < 18.5) :
        print('BMI = {}, BERAT BADAN KURANG'.format(bmi))
    elif(bmi >= 18.5 and bmi <= 24.9) :
        print('BMI = {}, BERAT BADAN IDEAL'.format(bmi))
    elif(bmi >= 25.0 and bmi <= 29.9) :
        print('BMI = {}, BERAT BADAN BERLEBIH'.format(bmi))
    elif(bmi >= 30.0 and bmi <= 39.9) :
        print('BMI = {}, BERAT BADAN SANGAT BERLEBIH'.format(bmi))
    elif(bmi >= 40) :
        print('BMI = {}, OBESITAS'.format(bmi))
    elif(bmi < 0) :
        print('Tidak menerima angka negatif')
except :
    print('Angka yg anda masukkan salah ')