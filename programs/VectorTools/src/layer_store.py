"""Przechowywanie wczytanej warstwy dla całego programu."""

from geopandas import GeoDataFrame


class LayerStore:
    def __init__(self) -> None:
        self._layer: GeoDataFrame | None = None
        self._name: str | None = None

    @property
    def layer(self) -> GeoDataFrame | None:
        return self._layer

    @property
    def name(self) -> str | None:
        return self._name

    def set_layer(self, layer: GeoDataFrame | None, name: str | None = None) -> None:
        self._layer = layer
        self._name = name

    def has_layer(self) -> bool:
        return self._layer is not None
