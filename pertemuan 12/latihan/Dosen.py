from person import *

class Dosen(person):
    gelar = ""
    jabatan = ""
    Gaji = 0
    
    def __init__(self, nama, gender, umur, gelar, Jabatan):
        super().__init__(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = Jabatan  
    def setGaji (self.Uang):
        self.Gaji += "Uang"
    def cetak(self):
        super().cetak()
        print("gelar \t\t: ", self.gelar,
              "\njabatan \t: ", self.jabatan,
              "\nGaji \t\t: Rp.", self.Gaji,
              "\n---------------------------------")
    
