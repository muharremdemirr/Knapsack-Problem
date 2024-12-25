import random

# Maksimum ağırlık sınırı ve ağırlık/değer çiftleri
maxWeight = 40
w_v = [[7, 10], [2, 15], [10, 5], [15, 8], [5, 20], [3, 10], [8, 7], [4, 17], [9, 5], [12, 3]]

# Ağırlık hesaplama fonksiyonu
def cal_w(array):
    return sum(item[0] for item in array)  # Her elemanın ağırlığını toplar

# Çaprazlama fonksiyonu
def cross(arr):
    offspring = []
    for i in range(0, len(arr), 2):
        if i + 1 < len(arr):  # Çift kontrolü
            crosspoint = random.randint(1, len(arr[0]) - 1)  # Çaprazlama noktası (1'den itibaren)
            of1 = arr[i + 1][crosspoint:] + arr[i][:crosspoint]
            of2 = arr[i][crosspoint:] + arr[i + 1][:crosspoint]
            offspring.extend([of1, of2])
    return offspring

# Rastgele başlangıç çözümleri oluştur
solutions = []
weights = []
for _ in range(10):  # 10 çözüm üret
    parent = []
    while len(parent) < 6:  # Her çözümde 6 öğe olsun
        rnd = random.randint(0, len(w_v) - 1)
        if w_v[rnd] not in parent:  # Tekrarlı elemanları engelle
            parent.append(w_v[rnd])
    solutions.append(parent)
    weights.append(cal_w(parent))

# Çözümleri yazdır
for w, (arr, weight) in enumerate(zip(solutions, weights)):
    val = 0 if weight <= maxWeight else 1000000  # Ağırlık sınırı aşılırsa yüksek ceza
    print(f"{w}: {arr}, weight: {weight}, value: {val}")

# Çaprazlama işlemi
print("****************child********************************")
offspring = cross(solutions)

# Çocukları yazdır
for i, child in enumerate(offspring):
    print(f"{i}: {child}, fitness: {cal_w(child)}")
