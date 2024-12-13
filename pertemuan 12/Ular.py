from Animal import *

print("========= Ular anaconda ============")
class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
        
    def cetak_ular(self):
        super().cetak()
        print("Design \t\t: ", self.design,
              "\nRacun \t\t: ", self.racun)
        
anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik Solo", "Tidak Beracun")
anaconda.cetak_ular()
print("========= Ular cobra ============")
piton = Ular("Piton", "Tikus", "Semak belukar/rawa-rawa", "Bertelur", "Batik", "Tidak Beracun")
piton.cetak_ular()