from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

dane = Path(__file__).parent / "dane"

# Dla warstwy z rzekami policz ile jest obiektów, których MultiLineString
# zawiera dokładnie między 2 a 10 części składowych geometrii.
rzeki = gpd.read_file(dane / "hr1.geojson")
print(rzeki.geometry.apply(lambda g: len(g.geoms)).between(2, 10).sum())

# Dla warstwy demograficznej wyświetl na mapie kraje, w których odsetek
# osób w wieku 65+ wynosi ponad 18%.
demografia = gpd.read_file(dane / "lsp1.geojson")
demografia["odsetek_65"] = pd.to_numeric(
    demografia["ludność_w_wieku_65_lat_i_więcej"].str.rstrip("% "),
    errors="coerce",
)
demografia[demografia["odsetek_65"] > 18].plot()
plt.show()

# Dla warstwy z wulkanami stwórz podzbiór wulkanów znajdujących się w Stanach
# Zjednoczonych. Następnie wypisz wszystkie typy wulkanów występujące w tym
# podzbiorze oraz oblicz, jaki procent wszystkich wulkanów w USA stanowi każdy z typów.
usa = gpd.read_file(dane / "wulkany" / "lw1" / "lw1.shp")
usa = usa[usa["kraj"] == "Stany Zjednoczone"]
print(usa["typ"].value_counts())
print(round((usa["typ"].value_counts(normalize=True) * 100)))
