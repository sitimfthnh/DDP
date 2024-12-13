from Animal import *

print("========= burung Hantu ============")
class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi
        
    def cetak_burung(self):
        super().cetak()
        print("jenis \t\t: ", self.jenis,
              "\nbunyi \t\t: ", self.bunyi)
        
Hantu = Burung("Hantu", "Daging", "Hutan", "Bertelur", "Serak Bukit", "Hoooooo")
Hantu.cetak_burung()
print("========= burung Kakak Tua ============")
Kakak_tua = Burung("kakak tua", "Biji bijian", "Hutan", "Bertelur", "kakatua galah", "wekwekwek")
Kakak_tua.cetak_burung()