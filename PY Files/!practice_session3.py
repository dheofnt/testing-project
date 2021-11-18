
# angka = [
#     #0  #1   #2  #3  #4
#     [1,  2,  3,  4,  5],  #0
#     [6,  7 , 8,  9,  10], #1
#     [11, 12, 13, 14, 15], #2
#     [16, 17, 18, 19, 20], #3
#     [21, 22, 23, 24, 25]  #4
# ]

# inputAngka = int(print('Masukkan angka 1-3 : '))
# [
#     [1,  2,  3,  4,  5],  
#     [6,  7 , 8,  9,  10], 
#     [11, 12, 13, 14, 15], 
#     [16, 17, 18, 19, 20], 
#     [21, 22, 23, 24, 25]  
# ]
# print(angka.index(1))


inputAngka1 = int and float(input('Masukkan Angka 1: '))
inputAngka2 = int and float(input('Masukkan Angka 2: '))
inputOperator = input('Masukkan Operator : ')

plus = inputAngka1 + inputAngka2
minus = inputAngka1 - inputAngka2
division = inputAngka1 / inputAngka2
multiple = inputAngka1 * inputAngka2
if inputOperator == '+' :
    print('Hasil dari {} + {} = {}'.format(inputAngka1, inputAngka2, plus))
elif inputOperator == '-' :
    print('Hasil dari {} + {} = {}'.format(inputAngka1, inputAngka2, minus))
elif inputOperator == '/' :
    print('Hasil dari {} + {} = {}'.format(inputAngka1, inputAngka2, division))
elif inputOperator == '*' :
    print('Hasil dari {} + {} = {}'.format(inputAngka1, inputAngka2, multiple))
