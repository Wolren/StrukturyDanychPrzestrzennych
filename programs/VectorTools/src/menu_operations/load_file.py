"""Operacja wczytująca punkty z pliku."""

import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox

from src import config
from src.column_dialog import ColumnDialog
from src.menu_operations.operation import MenuOperation
from src.plural import plural
from src.point import Point
from src.status_bar import StatusBar
from src.table_reader import Table, TableFileError, read_table


class LoadFile(MenuOperation):
    def __init__(self, parent: tk.Tk, status_bar: StatusBar) -> None:
        self._parent = parent
        self._status_bar = status_bar
        self._points: list[Point] = []

    @property
    def points(self) -> list[Point]:
        return self._points

    def execute(self) -> None:
        path = filedialog.askopenfilename(
            parent=self._parent,
            title=config.FILE_DIALOG_TITLE,
            filetypes=config.FILE_DIALOG_TYPES,
        )
        if not path:
            return

        try:
            points = self._read(path)
        except TableFileError as error:
            self._fail(error)
            return

        if points is None:
            return

        self._points = points

        count = len(points)
        word = plural(count, "punkt", "punkty", "punktów")
        self._status_bar.set(f"Wczytano {count} {word}: {Path(path).name}")

    def _read(self, path: str) -> list[Point] | None:
        table = read_table(path)
        columns = self._choose_columns(table)

        if columns is None:
            return None

        return table.to_points(*columns)

    def _choose_columns(self, table: Table) -> tuple[int, int] | None:
        if len(table.columns) == 2:
            return (0, 1)

        return ColumnDialog.ask(self._parent, table.columns)

    def _fail(self, error: TableFileError) -> None:
        self._points = []
        self._status_bar.set("Nie udało się wczytać pliku.")
        messagebox.showerror("Błąd wczytywania", str(error), parent=self._parent)
