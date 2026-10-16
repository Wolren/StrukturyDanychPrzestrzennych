"""Menu programu."""

import tkinter as tk

from src import config, layout
from src.menu_option import MenuOption
from src.menu_operations.operation import MenuOperation


class Menu:
    def __init__(self, canvas: tk.Canvas) -> None:
        self._canvas = canvas
        self._options: list[MenuOption] = []

    def add_option(self, label: str, operation: MenuOperation) -> MenuOption:
        option = MenuOption(self._canvas, label, operation)
        self._options.append(option)

        return option

    def draw(self, size: tuple[int, int]) -> None:
        self._canvas.create_text(
            *layout.scaled(config.MENU_HEADING_POSITION, size),
            text=config.MENU_HEADING,
            font=layout.scaled_font(config.HEADING_FONT, size),
            fill=config.TEXT_COLOR,
        )

        for index, option in enumerate(self._options):
            position = (
                config.MENU_X,
                config.MENU_FIRST_OPTION_Y + index * config.MENU_OPTION_SPACING,
            )
            option.draw(size, position)
