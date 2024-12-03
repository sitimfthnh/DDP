import Hitung
import LuasBangunDatar as Bangundatar
from LuasBangunRuang import (kubus, balok, tabung, limas, prisma)

# Modul Hitung
print("========= Modul Hitung ============")
Hitung.tambah(10, 20)
Hitung.kurang(20, 5)
Hitung.kali(5, 2)
Hitung.bagi(20, 5)
Hitung.pangkat(5, 2)

print("========== Modul Luas Bangun Datar ============")
# Modul Luass bangun datar
Bangundatar.luas_lingkaran(20)
Bangundatar.luas_persegi(15)
Bangundatar.luas_persegi_panjang(10)
Bangundatar.luas_segitiga(12)
Bangundatar.luas_jajar_genjang(10)

print("========== Modul Bangun Ruang ============")
# Modul Bangun Ruang
kubus(10)
balok(5)
tabung(7)
limas(15)
prisma(20)