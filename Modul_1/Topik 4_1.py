daftar_belanja = []

print("=== Program Daftar Belanja ===")

for i in range(3):
    barang = input(f"Masukkan barang ke-{i+1}: ")
    daftar_belanja.append(barang)

print("\n--- Daftar Belanja Anda ---")
print(daftar_belanja)
