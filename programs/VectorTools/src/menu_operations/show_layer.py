"""Operacja wyświetlająca warstwę na wykresie."""

import matplotlib.pyplot as plt
from geopandas import GeoDataFrame

from src import config
from src.layer_store import LayerStore
from src.menu_operations.operation import MenuOperation
from src.plural import plural
from src.status_bar import StatusBar


def color_column(layer: GeoDataFrame) -> str | None:
    name = config.LAYER_COLOR_COLUMN

    if name not in layer.columns or layer[name].nunique() < 2:
        return None

    return name


class ShowLayer(MenuOperation):
    def __init__(self, store: LayerStore, status_bar: StatusBar) -> None:
        self._store = store
        self._status_bar = status_bar

    def execute(self) -> None:
        layer = self._store.layer
        if layer is None:
            self._status_bar.set("Najpierw wczytaj warstwę.")
            return

        plt.close("all")

        column = color_column(layer)
        if column is None:
            axes = layer.plot()
        else:
            axes = layer.plot(column=column, legend=True, cmap=config.LAYER_COLORMAP)

        axes.set_title(self._title(layer))
        # block=False, inaczej show() zawiesza pętlę zdarzeń tkintera.
        plt.show(block=False)

    def _title(self, layer: GeoDataFrame) -> str:
        count = len(layer)
        word = plural(count, "obiekt", "obiekty", "obiektów")

        if self._store.name is None:
            return f"{count} {word}"

        return f"{self._store.name} - {count} {word}"
