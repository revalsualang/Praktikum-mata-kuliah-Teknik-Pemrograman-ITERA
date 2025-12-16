class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama          # public
        self.__nim = nim          # private

    def tampilkan_data(self):
        print("Nama:", self.nama)
        print("NIM :", self.__nim)

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim_baru):
        self.__nim = nim_baru

mhs = Mahasiswa("Reval", "12345678")

mhs.tampilkan_data()

mhs.set_nim("124120022")

print("\nSetelah NIM diubah:")
mhs.tampilkan_data()
