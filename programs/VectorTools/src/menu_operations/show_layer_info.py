"""Operacja pokazująca informacje o wczytanej warstwie."""

from tkinter import messagebox

from geopandas import GeoDataFrame

from src.layer_store import LayerStore
from src.menu_operations.operation import MenuOperation


def layer_info(layer: GeoDataFrame) -> str:
    return (
        f"Liczba obiektów: {len(layer)}\n"
        f"Liczba kolumn: {len(layer.columns)}\n"
        f"Typ geometrii: {', '.join(layer.geom_type.unique())}\n"
        f"Układ współrzędnych: {layer.crs}"
    )


class ShowLayerInfo(MenuOperation):
    def __init__(self, store: LayerStore) -> None:
        self._store = store

    def execute(self) -> None:
        layer = self._store.layer
        if layer is None:
            return

        messagebox.showinfo("Informacje o warstwie", layer_info(layer))
