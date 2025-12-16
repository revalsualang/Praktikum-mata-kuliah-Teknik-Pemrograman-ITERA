with open("laporan_awal.txt", "w") as file:
    file.write("LAPORAN PRAKTIKUM MODUL 4\n")
    file.write("========================\n")
    file.write("Ini adalah contoh file handling.\n")

with open("laporan_awal.txt", "a") as file:
    file.write("Baris tambahan hasil append.\n")

try:
    with open("laporan_awal.txt", "r") as file:
        print("Isi file:")
        print(file.read())
except FileNotFoundError:
    print("File tidak ditemukan.")
