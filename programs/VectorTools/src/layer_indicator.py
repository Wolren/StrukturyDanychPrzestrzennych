"""Potwierdzenie, że warstwa jest wczytana."""

import tkinter as tk

from src import config, layout
from src.layer_store import LayerStore


class LayerIndicator:
    def __init__(self, canvas: tk.Canvas, store: LayerStore) -> None:
        self._canvas = canvas
        self._store = store

    def draw(self, size: tuple[int, int]) -> None:
        if not self._store.has_layer():
            return

        self._canvas.create_text(
            *layout.scaled(config.LAYER_STATUS_POSITION, size),
            text=config.LAYER_STATUS_TEXT,
            font=layout.scaled_font(config.LAYER_STATUS_FONT, size),
            fill=config.LAYER_STATUS_COLOR,
            tags=config.LAYER_STATUS_TAG,
        )

    def refresh(self) -> None:
        self._canvas.delete(config.LAYER_STATUS_TAG)
        size = (self._canvas.winfo_width(), self._canvas.winfo_height())

        self.draw(size)
