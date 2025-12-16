data_mahasiswa = [
    {"nama": "Reval", "nilai": 85},
    {"nama": "Budi", "nilai": 78},
    {"nama": "Citra", "nilai": 90},
    {"nama": "Dina", "nilai": 88}
]

print("Data Nilai Mahasiswa:")
for mhs in data_mahasiswa:
    print(f"{mhs['nama']} : {mhs['nilai']}")

total = 0
for mhs in data_mahasiswa:
    total += mhs["nilai"]

rata_rata = total / len(data_mahasiswa)
print("\nNilai rata-rata:", rata_rata)

nilai_tertinggi = max(data_mahasiswa, key=lambda x: x["nilai"])
print("Nilai tertinggi:", nilai_tertinggi["nama"], "-", nilai_tertinggi["nilai"])
