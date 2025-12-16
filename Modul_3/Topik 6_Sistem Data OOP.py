class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    def kelulusan(self):
        if self.nilai >= 60:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def tampilkan_data(self):
        print(f"Nama  : {self.nama}")
        print(f"NIM   : {self.nim}")
        print(f"Nilai : {self.nilai}")
        print(f"Status: {self.kelulusan()}")
        print("-" * 30)

daftar_mahasiswa = [
    Mahasiswa("Reval", "124120022", 80),
    Mahasiswa("Naomi", "124120059", 55),
    Mahasiswa("Calvin", "124120040", 90)
]

for mhs in daftar_mahasiswa:
    mhs.tampilkan_data()
