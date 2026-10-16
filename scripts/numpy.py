import numpy as np

# Stwórz losową 1-wymiarową numpy array o długości 15 elementów.
# Następnie oblicz jej minimum, maksimum oraz odchylenie standardowe.
arr = np.random.randint(1, 100, 15)
print("min:", arr.min())
print("max:", arr.max())
print("std:", arr.std(), "\n\n")

# Stwórz losową tablicę 2-wymiarową numpy array 4 wiersze x 4 kolumny,
# a następnie oblicz sumę wartości dla każdej kolumny oraz dla każdego wiersza.
matrix = np.random.randint(1, 100, (4, 4))
print("sumy wierszy:", matrix.sum(axis=1))
print("sumy kolumn:", matrix.sum(axis=0), "\n\n")

# Stwórz tablicę 2-wymiarową 5 wierszy x 5 kolumn, w której każda wartość
# będzie o 3 większa od poprzedniej. Podaj indeksy każdej wartości parzystej większej od 10.
seq = np.arange(0, 75, 3).reshape(5, 5)
for i in range(5):
    for j in range(5):
        if seq[i, j] > 10 and seq[i, j] % 2 == 0:
            print("indeks:", i, j)
