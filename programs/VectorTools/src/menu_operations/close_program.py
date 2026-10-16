"""Operacja zamykająca program."""

import tkinter as tk

from src.menu_operations.operation import MenuOperation


class CloseProgram(MenuOperation):
    def __init__(self, window: tk.Tk) -> None:
        self._window = window

    def execute(self) -> None:
        self._window.after(0, self._window.destroy)
