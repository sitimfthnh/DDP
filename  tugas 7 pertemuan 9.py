#Soal No 1
print('---- mencari celcius ke fahrenheit ----')
def celcius_ke_fahrenheit (celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

#Soal No 2
print('\n---- mencari bilangan genap ----')
def is_genap(bil_genap):
    return bil_genap %2 == 0
#untuk memasukan value
print(is_genap(4))
print(is_genap(7))

#Soal No 3
print('\n---- mencari nilai kelulusan----')
# rata" nilai 70
def nilai_kelulusan(nilai):
    if nilai >= 80:
        return 'lulus'
    else :
        return 'gagal'
#untuk mencetak value
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))

#Soal No 4
print('\n---- cetak bilangan ganjil ----')
def bil_ganjil(angka):
    for i in range(1, angka, 2):
        print(i, end=" ")
#untuk memasukan velue
bil_ganjil(20)


    