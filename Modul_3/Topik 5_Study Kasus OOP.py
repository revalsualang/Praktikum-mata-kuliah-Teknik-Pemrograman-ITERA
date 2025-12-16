class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def status_kelulusan(self):
        if self.nilai >= 60:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    def tampilkan_data(self):
        print(f"Nama  : {self.nama}")
        print(f"Nilai : {self.nilai}")
        print(f"Status: {self.status_kelulusan()}")
        print("-" * 30)

mhs1 = Mahasiswa("Reval", 75)
mhs2 = Mahasiswa("Naomi", 55)
mhs3 = Mahasiswa("Calvin", 90)

mhs1.tampilkan_data()
mhs2.tampilkan_data()
mhs3.tampilkan_data()
