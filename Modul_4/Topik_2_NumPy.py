import numpy as np

data = np.array([2, 4, 6, 8, 10])

print("Array:", data)
print("Jumlah:", np.sum(data))
print("Rata-rata:", np.mean(data))
print("Nilai maksimum:", np.max(data))
print("Nilai minimum:", np.min(data))

print("\nData dikali 2:", data * 2)
print("Data ditambah 5:", data + 5)

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nMatrix 2D:")
print(matrix)
print("Transpose matrix:")
print(matrix.T)
