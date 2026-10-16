import pandas as pd

# Utwórz DataFrame zawierający dane 10 osób, wzrost w centymetrach
# oraz masę ciała w kilogramach. Następnie na podstawie tych danych
# wygeneruj kolumnę zawierającą BMI każdej osoby.
df = pd.DataFrame({
    "name": ["Adam", "Beata", "Celina", "Dawid", "Ewa", "Filip", "Greta", "Henryk", "Iwona", "Jakub"],
    "height": [180, 165, 172, 190, 158, 176, 169, 183, 160, 178],
    "weight": [82, 58, 70, 95, 52, 68, 60, 88, 55, 74]
})
df["bmi"] = df["weight"] / (df["height"] / 100) ** 2
print(df)

# Utwórz własny DataFrame zawierający wybrane przez siebie dane.
# Zapisz go do pliku JSON, a następnie wczytaj ten plik do nowego
# obiektu DataFrame. Sprawdź, czy oba obiekty zawierają te same dane.
df_custom = pd.DataFrame({
    "country": ["Polska", "Niemcy", "Francja"],
    "population": [38, 84, 68],
    "area": [312696, 357588, 551695]
})
df_custom.to_json("data.json", orient="records", indent=2)
df_loaded = pd.read_json("data.json")
print(df_loaded)
print(df_custom.equals(df_loaded))

# Wykorzystaj DataFrame stworzony w punkcie 1. Dodaj kolumnę z wiekiem
# i wypełnij ją danymi. Następnie znajdź osoby starsze niż średnia wieku
# wszystkich osób, których BMI jest jednocześnie większe niż 25.
# Wyświetl imiona, wiek oraz BMI tych osób.
df["age"] = [25, 31, 28, 42, 35, 29, 61, 33, 27, 45]
result = df[(df["age"] > df["age"].mean()) & (df["bmi"] > 25)]
print(result[["name", "age", "bmi"]])
