"""Tło ekranu startowego programu."""

import tkinter as tk
from pathlib import Path

from PIL import Image, ImageTk


def cover_box(size: tuple[int, int], target: tuple[int, int]) -> tuple[int, int, int, int]:
    width, height = size
    target_width, target_height = target

    if width * target_height > target_width * height:
        new_width = round(height * target_width / target_height)
        left = (width - new_width) // 2
        return (left, 0, left + new_width, height)

    new_height = round(width * target_height / target_width)
    top = (height - new_height) // 2
    return (0, top, width, top + new_height)


class BackgroundImage:
    def __init__(self, canvas: tk.Canvas, image_path: Path) -> None:
        self._canvas = canvas
        self._image_path = image_path
        self._source: Image.Image | None = None
        self._image: ImageTk.PhotoImage | None = None

    def draw(self, size: tuple[int, int]) -> None:
        if not self._image_path.exists():
            return

        # Referencja musi żyć w atrybucie, inaczej tkinter usuwa obraz z pamięci.
        self._image = ImageTk.PhotoImage(self._prepare(size))
        self._canvas.create_image(0, 0, image=self._image, anchor="nw")

    def _prepare(self, size: tuple[int, int]) -> Image.Image:
        source = self._load_source()

        return source.crop(cover_box(source.size, size)).resize(size, Image.Resampling.LANCZOS)

    def _load_source(self) -> Image.Image:
        if self._source is None:
            with Image.open(self._image_path) as opened:
                self._source = opened.convert("RGB")

        return self._source
