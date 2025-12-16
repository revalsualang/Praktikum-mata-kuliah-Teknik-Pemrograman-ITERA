class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

    def tampilkan_data(self):
        print(f"Nama  : {self.nama}")
        print(f"NIM   : {self.nim}")
        print(f"Prodi : {self.prodi}")
        print("-" * 30)

m1 = Mahasiswa("Reval", "124120022", "Teknik Geofisika")
m2 = Mahasiswa("Naomi", "124120059", "Teknik Geofisika")

m1.tampilkan_data()
m2.tampilkan_data()
