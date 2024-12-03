# Membuat Modul Untuk Menghitung Luas Bangun Ruang

def kubus(rusuk):
    hasil = rusuk**3
    print(f'Hasil dari luas volume kubus {rusuk} = {hasil}')

def balok(panjang_lebar_tinggi):
    hasil = panjang_lebar_tinggi*2
    print(f'Hasil dari luas volume balok {panjang_lebar_tinggi} = {hasil}')
    
def tabung(jari_jari_tinggi):
    phi = 3.14
    hasil = phi*jari_jari_tinggi*2
    print(f'Hasil dari luas volume tabung {jari_jari_tinggi} = {hasil}')

def limas(alas_tinggi): 
    hasil = (1/3) * alas_tinggi
    print(f'Hasil dari luas volume limas {alas_tinggi} = {hasil}')
    
def prisma(alas_tinggi_tinggiPrisma):
    hasil = 1/2*alas_tinggi_tinggiPrisma 
    print(f'Hasil dari luas Volume prisma {alas_tinggi_tinggiPrisma} = {hasil}')