mahasiswa = {
    "nama": "Reval LD Sualang",
    "nim": "124120022",
    "nilai": {
        "Fisika Matematika": 85,
        "Petrofisika": 90,
        "Teknik Pemrograman": 95
    }
}

print("Nama:", mahasiswa["nama"])
print("NIM:", mahasiswa["nim"])

print("\nNilai Mata Kuliah:")
for matkul, nilai in mahasiswa["nilai"].items():
    print(f"{matkul} : {nilai}")

print("\nNilai Teknik Pemrograman:", mahasiswa["nilai"]["Teknik Pemrograman"])
