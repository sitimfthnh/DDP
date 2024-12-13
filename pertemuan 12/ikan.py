from Animal import *

print("========= Ikan koki ============")
class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bentukTubuh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bentukTubuh = bentukTubuh
        
    def cetak_Ikan(self):
        super().cetak()
        print("jenis \t\t: ", self.jenis,
              "\nbentukTubuh \t: ", self.bentukTubuh)
        
koki = Ikan("koki", "Serangga kecil/jentik nyamuk", "Air Tawar", "Bertelur", "Koki Ryukin", "pendek dan kekar")
koki.cetak_Ikan()
print("========= Ikan Arwana ============")
Arwana = Ikan("Arwana", "Pelet,Ikan hidup,Serangga", "sungai/danau", "Bertelur", "Super Red", "Pipih, Memenjang dan Ramping ")
Arwana.cetak_Ikan()