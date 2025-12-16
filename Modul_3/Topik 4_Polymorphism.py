class Mahasiswa:
    def tampilkan_peran(self):
        print("Saya adalah mahasiswa")

class Asisten(Mahasiswa):
    def tampilkan_peran(self):
        print("Saya adalah asisten praktikum")

class Dosen(Mahasiswa):
    def tampilkan_peran(self):
        print("Saya adalah dosen")

daftar = [
    Mahasiswa(),
    Asisten(),
    Dosen()
]

for orang in daftar:
    orang.tampilkan_peran()
