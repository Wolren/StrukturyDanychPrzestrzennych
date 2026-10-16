"""Pojedyncza pozycja w menu programu."""

import tkinter as tk

from src import config, layout
from src.menu_operations.operation import MenuOperation


class MenuOption:
    def __init__(self, canvas: tk.Canvas, label: str, operation: MenuOperation) -> None:
        self._canvas = canvas
        self._label = label
        self._operation = operation
        self._item_id: int | None = None

    def draw(self, size: tuple[int, int], position: tuple[int, int]) -> None:
        self._item_id = self._canvas.create_text(
            *layout.scaled(position, size),
            text=self._label,
            font=layout.scaled_font(config.OPTION_FONT, size),
            fill=config.TEXT_COLOR,
        )

        self._canvas.tag_bind(self._item_id, "<Button-1>", self._on_click)
        self._canvas.tag_bind(self._item_id, "<Enter>", self._on_enter)
        self._canvas.tag_bind(self._item_id, "<Leave>", self._on_leave)

    def _on_click(self, _event: tk.Event) -> None:
        self._operation.execute()

    def _on_enter(self, _event: tk.Event) -> None:
        self._set_color(config.TEXT_HOVER_COLOR)

    def _on_leave(self, _event: tk.Event) -> None:
        self._set_color(config.TEXT_COLOR)

    def _set_color(self, color: str) -> None:
        self._canvas.itemconfig(self._item_id, fill=color)
