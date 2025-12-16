from scipy import stats
import numpy as np

data = np.array([85, 78, 90, 88, 92, 75])

print("Data:", data)

print("Rata-rata:", np.mean(data))
print("Median:", np.median(data))
print("Standar deviasi:", np.std(data))

modus = stats.mode(data, keepdims=True)
print("Modus:", modus.mode[0])

t_stat, p_value = stats.ttest_1samp(data, popmean=80)

print("\nHasil uji t satu sampel")
print("t-statistik:", t_stat)
print("p-value:", p_value)
