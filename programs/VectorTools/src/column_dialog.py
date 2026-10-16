"""Okno wyboru kolumn ze współrzędnymi."""

import tkinter as tk
from collections.abc import Sequence
from tkinter import ttk

from src import config


class ColumnDialog(tk.Toplevel):
    def __init__(self, parent: tk.Misc, columns: Sequence[str]) -> None:
        super().__init__(parent)

        self._columns = list(columns)
        self._labels = [f"{index + 1}. {name}" for index, name in enumerate(self._columns)]
        self._choice: tuple[int, int] | None = None

        self.title(config.COLUMN_DIALOG_TITLE)
        self.resizable(False, False)
        self.transient(parent)
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        self._build()
        self.wait_visibility()
        self.grab_set()
        self.focus_set()

    @property
    def choice(self) -> tuple[int, int] | None:
        return self._choice

    @classmethod
    def ask(cls, parent: tk.Misc, columns: Sequence[str]) -> tuple[int, int] | None:
        dialog = cls(parent, columns)
        dialog.wait_window()

        return dialog.choice

    def _build(self) -> None:
        self._x_var = tk.StringVar()
        self._y_var = tk.StringVar()

        fields = (
            ("Kolumna X:", self._x_var),
            ("Kolumna Y:", self._y_var),
        )
        for row, (text, variable) in enumerate(fields):
            tk.Label(self, text=text).grid(row=row, column=0, sticky="w", padx=10, pady=4)
            ttk.Combobox(
                self,
                textvariable=variable,
                values=self._labels,
                state="readonly",
                width=30,
            ).grid(row=row, column=1, padx=10, pady=4)
            variable.trace_add("write", self._update_submit)

        self._submit = tk.Button(self, text="Wczytaj", state="disabled", command=self._accept)
        self._submit.grid(row=len(fields), column=0, padx=10, pady=(8, 10))
        tk.Button(self, text="Anuluj", command=self.destroy).grid(
            row=len(fields), column=1, padx=10, pady=(8, 10)
        )

    def _update_submit(self, *_args: str) -> None:
        filled = bool(self._x_var.get()) and bool(self._y_var.get())
        self._submit.config(state="normal" if filled else "disabled")

    def _accept(self) -> None:
        self._choice = (
            self._labels.index(self._x_var.get()),
            self._labels.index(self._y_var.get()),
        )
        self.destroy()
