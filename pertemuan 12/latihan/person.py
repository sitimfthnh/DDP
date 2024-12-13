class person:
    def __init__(self, nama, gender, umur):
        self.nama = nama
        self.gender = gender
        self.umur = umur
    
    def cetak(self):
        print("Nama \t\t: ", self.nama,
              "\ngender \t: ", self.gender,
              "\numur \t\t: ", self.umur,
        )
        
        