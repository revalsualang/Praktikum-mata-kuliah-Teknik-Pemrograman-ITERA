class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkan_data(self):
        print(f"Nama : {self.nama}")
        print(f"NIM  : {self.nim}")

class MahasiswaAktif(Mahasiswa):
    def __init__(self, nama, nim, semester):
        super().__init__(nama, nim)
        self.semester = semester

    def tampilkan_data(self):
        super().tampilkan_data()
        print(f"Semester : {self.semester}")
        print("-" * 30)

mhs1 = MahasiswaAktif("Reval", "124120022", 3)
mhs2 = MahasiswaAktif("Naomi", "124120059", 4)

mhs1.tampilkan_data()
mhs2.tampilkan_data()
