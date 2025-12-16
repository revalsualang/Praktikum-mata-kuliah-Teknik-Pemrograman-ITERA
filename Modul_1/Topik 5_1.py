angka_rahasia = 17

print("=== Permainan Tebak Angka ===")

while True:
    tebakan = int(input("Masukkan tebakan anda: "))

    if tebakan < angka_rahasia:
        print("Tebakan terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Tebakan terlalu besar!")
    else:
        print("Selamat! Tebakan anda benar 🎉")
        break
