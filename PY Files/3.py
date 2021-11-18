hari = {
    "senin" : "monday",
    "selasa" : "tuesday",
    "rabu" : "wednesday",
    "kamis" : "thursday",
    "jumat" : "friday",
    "sabtu" : "saturday",
    "minggu" : "sunday"
}

# print(list(hari.values()))

# print(list(hari.keys()))

# hari_Indo = list(hari.keys())
# hari_Eng = list(hari.values())
# # Hari_Input = 'friday'

# # # print(hari_Indo[hari_Eng.index(Hari_Input)])

# Hari_Input = input("Masukkan nama Hari : ").lower()

# # if Hari_Input in hari_Indo:
# #     print(hari[Hari_Input])
# # elif Hari_Input in hari_Eng:
# #     print(hari_Indo[hari_Eng.index(Hari_Input)])
# # else:
# #     print("nama hari Tidak ada")

# for i, j in hari.items():

#     if Hari_Input == i:
#         print(j)
#         break
#     elif Hari_Input == j:
#         print(i)
#         break
# else:
#     print("Nama hari Tidak Ada")

# kalimat = input("Masukkan kalimat : ")

# ## Reverse Tiap kata
# # print(kalimat[::-1])

# Kata = kalimat.split(" ")
# Reverse = []
# for i in Kata:
#     Reverse.append(i[::-1])
# print(" ".join(Reverse))

# print(3%7)

# hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
# senin = 0
# jumlah = 3

# Hari_I = input("Masukkan nama Hari : ")
# jumlah = int(input("Masukkan Jumlah : "))
# Index_O = hari.index(Hari_I) + jumlah
# if Index_O > 6:
#     Index_O = Index_O%7

# print(hari[Index_O])

List_Awal = [
    [1,2,3,4,5], #0
    [6,7,8,9,10], #1
    [11,12,13,14,15], #2
    [16,17,18,19,20], #3
    [21,22,23,24,25] #4 
]

# Output dari Opsi 1
# [
#     [21,16,11,6,1],
#     [22,17,12,7,2],
#     [23,18,13,8,3],
#     [24,19,14,9,4],
#     [25,20,15,10,5]
# ]


# [
#     [21, 16, 11, 6, 1], 
#     [22, 17, 12, 7, 2], 
#     [23, 18, 13, 8, 3], 
#     [24, 19, 14, 9, 4], 
#     [25, 20, 15, 10, 5]
#     ]

[
    [21, 16, 11, 6, 1], 
    [22, 17, 12, 7, 2], 
    [23, 18, 13, 8, 3], 
    [24, 19, 14, 9, 4], 
    [25, 20, 15, 10, 5]
    ]

# print(List_Awal[4][2])
# print(List_Awal[1][4])
# print(List_Awal[3][2])
# [
#     [4.0, 3.0, 2.0, 1.0, 0.0],  akan mengisi List Index [0.0, 0.1, 0.2, 0.3, 0.4]
#     [4.1, 3.1, 2.1, 1.1, 0.1],
#     [4.2, 3.2, 2.2, 1.2, 0.2],
#     [4.3, 3.3, 2.3, 1.3, 0.3],
#     [4.4, 3.4, 2.4, 1.4, 0.4]
# ]

# 4 3 2 1 0
# 0 1 2 3 4

# for i in range(5): ### 0 1 2 3 4
#     print(i)

# for i in range(4,-1,-1): ### 4 3 2 1 0
#     print(i)

# def Spinner(Awal):

#     List_Akhir = [
#         [0,0,0,0,0],
#         [0,0,0,0,0],
#         [0,0,0,0,0],
#         [0,0,0,0,0],
#         [0,0,0,0,0]
#     ]

#     for i in range(5):
#         for j in range(4, -1, -1): ## 4 3 2 1 0 ===> 0 1 2 3 4
#             angka = 4 - j
#             List_Akhir[i][angka] = Awal[j][i]
#     return List_Akhir
#         # print((j, i))

# # print(List_Akhir)

# print(Spinner(List_Awal))

angka = int(input("Masukkan angka : "))
angka2 = int(input("Masukkan Angka : "))
ops = input("Masukkan Operator : ")
def penjumlahan(angka, angka2, ops):
    if ops == '+':
        hasil = angka + angka2
    elif ops == '-':
        hasil = angka - angka2
    elif ops == '*':
        hasil = angka * angka2
    elif ops == '/':
        hasil = angka / angka2
    else:
        print('Mohon untuk input Operator seperti "+ - / *"') 
    return hasil



print(penjumlahan(angka, angka2, ops))