import kalkulator_lib

print("=== Kalkulator Sederhana ===")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
print("5. Pangkat")

pilihan = input("Pilih operasi (1-5): ")

a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

if pilihan == "1":
    hasil = kalkulator_lib.tambah(a, b)
elif pilihan == "2":
    hasil = kalkulator_lib.kurang(a, b)
elif pilihan == "3":
    hasil = kalkulator_lib.kali(a, b)
elif pilihan == "4":
    hasil = kalkulator_lib.bagi(a, b)
elif pilihan == "5":
    hasil = kalkulator_lib.pangkat(a, b)
else:
    hasil = "Pilihan tidak valid!"

print("Hasil:", hasil)
