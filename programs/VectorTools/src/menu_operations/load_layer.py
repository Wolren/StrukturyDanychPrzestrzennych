"""Operacja wczytująca warstwę GIS z pliku."""

from pathlib import Path
from tkinter import filedialog, messagebox

import geopandas as gpd

from src import config
from src.layer_indicator import LayerIndicator
from src.layer_store import LayerStore
from src.menu_operations.operation import MenuOperation
from src.plural import plural
from src.status_bar import StatusBar

MESSAGE = (
    "Nie udało się wczytać wybranego pliku.\n"
    "Upewnij się, że jest to prawidłowy plik GIS."
)


class LoadLayer(MenuOperation):
    def __init__(self, store: LayerStore, indicator: LayerIndicator, status_bar: StatusBar) -> None:
        self._store = store
        self._indicator = indicator
        self._status_bar = status_bar

    def execute(self) -> None:
        path = filedialog.askopenfilename(
            title=config.LAYER_DIALOG_TITLE,
            filetypes=config.LAYER_DIALOG_TYPES,
        )
        if not path:
            return

        try:
            layer = gpd.read_file(path)
        except Exception:  # pylint: disable=broad-except
            self._status_bar.set("Nie udało się wczytać warstwy.")
            messagebox.showwarning("Błąd wczytywania", MESSAGE)
            return

        self._store.set_layer(layer, Path(path).name)
        self._indicator.refresh()

        count = len(layer)
        word = plural(count, "obiekt", "obiekty", "obiektów")
        self._status_bar.set(f"Wczytano warstwę: {Path(path).name} ({count} {word})")
