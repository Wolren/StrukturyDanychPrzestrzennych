"""Pasek statusu na dole okna."""

import tkinter as tk

from src import config, layout


class StatusBar:
    def __init__(self, canvas: tk.Canvas) -> None:
        self._canvas = canvas
        self._message = ""
        self._item_id: int | None = None

    def set(self, message: str) -> None:
        self._message = message

        if self._item_id is not None:
            self._canvas.itemconfig(self._item_id, text=message)

    def draw(self, size: tuple[int, int]) -> None:
        self._item_id = self._canvas.create_text(
            *layout.scaled(config.STATUS_POSITION, size),
            text=self._message,
            font=layout.scaled_font(config.STATUS_FONT, size),
            fill=config.TEXT_COLOR,
            anchor="sw",
        )
