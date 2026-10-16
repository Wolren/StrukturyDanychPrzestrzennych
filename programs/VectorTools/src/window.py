"""Główne okno aplikacji VectorTools."""

import tkinter as tk
from collections.abc import Callable

from src import config, layout
from src.background import BackgroundImage

Size = tuple[int, int]
Relayout = Callable[[Size], None]


class MainWindow:
    def __init__(self) -> None:
        self._root = tk.Tk()
        self._root.title(config.TITLE)
        self._root.minsize(config.WINDOW_MIN_WIDTH, config.WINDOW_MIN_HEIGHT)

        self._canvas = tk.Canvas(
            self._root,
            width=config.WINDOW_WIDTH,
            height=config.WINDOW_HEIGHT,
            highlightthickness=0,
            bg=config.BACKGROUND_PLACEHOLDER_COLOR,
        )
        self._canvas.pack(fill="both", expand=True)

        self._background = BackgroundImage(self._canvas, config.BACKGROUND_IMAGE)
        self._listeners: list[Relayout] = []
        self._last_size: Size | None = None
        self._resize_job: str | None = None

        self._canvas.bind("<Configure>", self._on_configure)

    @property
    def root(self) -> tk.Tk:
        return self._root

    @property
    def canvas(self) -> tk.Canvas:
        return self._canvas

    def add_resize_listener(self, listener: Relayout) -> None:
        self._listeners.append(listener)

    def run(self) -> None:
        self._root.mainloop()

    def _on_configure(self, _event: tk.Event) -> None:
        if self._resize_job is None:
            self._resize_job = self._root.after(config.RESIZE_DELAY, self._relayout)

    def _relayout(self) -> None:
        self._resize_job = None
        size = (self._canvas.winfo_width(), self._canvas.winfo_height())

        if size[0] < 2 or size[1] < 2 or size == self._last_size:
            return

        self._last_size = size

        self._canvas.delete("all")
        self._background.draw(size)
        self._draw_title(size)

        for listener in self._listeners:
            listener(size)

    def _draw_title(self, size: Size) -> None:
        self._canvas.create_text(
            *layout.scaled(config.TITLE_POSITION, size),
            text=config.TITLE,
            font=layout.scaled_font(config.TITLE_FONT, size),
            fill=config.TEXT_COLOR,
        )
