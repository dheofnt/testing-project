4.
Input : 
Masukkan Jumlah Hari : ... 
Output :
Nyatakan Jumlah hari tsb dalam 
... Tahun ... Bulan ... Minggu ... Hari 

Contoh :
Masukkan Jumlah Hari : 35
Output :
00 Tahun 01 Bulan 00 Mingu 05 hari 

Ketentuan :
- Format Output dalam 2 digit
- 1 tahun = 365 hari 
- 1 bulan = 30 hari 
- Jumlah hari Maksimal 4000 ==> Jika diatas 4000 Keluar Notif : Jumlah Hari diatas batas
- Tidak menerima nilai dibawah Nol (angka negatif) ==> Jika inputan angka negatif keluar notif :  Jumlah hari dibawah batas 
- Tidak bisa menerima String/text atau angka desimal ==> Notif : Jumlah hari yg anda masukkan Salah.

5. 
Hitung BMI (Body Mass Index)
Rumus BMI : massa(kg) / (tinggi (meter) pangkat 2)

Input :
Masukkan Tinggi Badan (dalam cm):
Masukkan Berat Badan (dalam kg) :
Outputnya :
Tinggi badan anda ... (meter) dan Berat Anda .... kg BMI anda ... (nilai BMI) dan anda termasuk .... (sesuai kondisi)

Kondisi :
BMI < 18.5 ==> Berat badan Kurang 
18.5 - 24.9 ==> Berat badan Ideal 
25 - 29.9 ==> Berat badan berlebih
30 - 39.9 ==> Berat badan sangat berlebih 
BMI >= 40 ==> Obesitas 

Ketentuan :
- Nilai BMI pada output dibulatkan 2 angka desimal 
- Nilai tinggi dan massa/berat tidak menerima angka negatif ==> Notif : Tidak menerima angka negatif 
- Tidak menerima Angka desimal atau String/text ==> Notif : Angka yg anda masukkan salah 
- Batas Maksimal Tinggi badan : 300cm, batas maksimal berat badan : 250kg ==> Notif : "Tinggi/Berat anda diatas batas"
- Notifikasi keluar setelah User input Tinggi dan Berat badan. 

6. 
Input 
Masukkan Nilai : ... 80,5  80.5

Output :
Nilai anda ... dan anda .... (sesuai kondisi)

Kondisi :
90 keatas : Grade A 
85 Keatas : Grade A- 
80 Keatas : Grade B
75 Keatas : Grade B-
70 Keatas : Grade C
65 Keatas : Grade D
dibawah 65 dan diatas 40 : Perlu Remedial
dibawah 40 : Tidak Lulus 

Ketentuan :
- Nilai Maksimum 100, nilai minimum 0
- Jika nilai diatas 100 : Notif : Nilai diluar jangkauan
- Jika nilai dibawah 0 : Notif : Tidak menerima angka Negatif 
- Jika nilai bukan angka/String : Angka yg anda masukkan Salah 
- Dapat menerima Nilai Desimal