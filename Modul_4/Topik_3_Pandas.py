import pandas as pd

data = {
    "Nama": ["Reval", "Naomi", "Calvin", "Putu"],
    "Nilai": [85, 78, 90, 88]
}

df = pd.DataFrame(data)

print("Data Mahasiswa:")
print(df)

print("\nRata-rata nilai:", df["Nilai"].mean())
print("Nilai tertinggi:", df["Nilai"].max())
print("Nilai terendah:", df["Nilai"].min())

print("\nMahasiswa dengan nilai >= 85:")
print(df[df["Nilai"] >= 85])

df.to_csv("data_mahasiswa.csv", index=False)
