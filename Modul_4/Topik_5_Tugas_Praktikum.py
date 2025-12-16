import numpy as np
import pandas as pd
from scipy import stats

data_nilai = np.array([80, 75, 90, 85, 88, 70])

rata_rata = np.mean(data_nilai)
median = np.median(data_nilai)
std_dev = np.std(data_nilai)
modus = stats.mode(data_nilai, keepdims=True).mode[0]

df = pd.DataFrame({
    "Nilai": data_nilai
})

df.to_csv("hasil_nilai_modul4.csv", index=False)

with open("laporan_modul4.txt", "w") as file:
    file.write("LAPORAN PRAKTIKUM MODUL 4\n")
    file.write("========================\n")
    file.write(f"Data nilai      : {data_nilai.tolist()}\n")
    file.write(f"Rata-rata       : {rata_rata}\n")
    file.write(f"Median          : {median}\n")
    file.write(f"Standar Deviasi : {std_dev}\n")
    file.write(f"Modus           : {modus}\n")

# Output ke terminal
print("=== HASIL ANALISIS DATA ===")
print("Data nilai:", data_nilai)
print("Rata-rata:", rata_rata)
print("Median:", median)
print("Standar Deviasi:", std_dev)
print("Modus:", modus)
print("\nFile CSV dan laporan teks berhasil dibuat.")
