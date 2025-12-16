mahasiswa = {
    "nama": "Reval LD Sualang",
    "nim": "124120022",
    "prodi": "Teknik Geofisika",
    "angkatan": 2024
}

print("Data Mahasiswa:")
for key, value in mahasiswa.items():
    print(f"{key} : {value}")

mahasiswa["ipk"] = 3.75

mahasiswa["angkatan"] = 2024

print("\nData setelah ditambah dan diubah:")
for key, value in mahasiswa.items():
    print(f"{key} : {value}")
