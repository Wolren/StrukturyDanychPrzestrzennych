"""Wczytywanie tabel z plików tekstowych."""

from dataclasses import dataclass
from pathlib import Path

from src.point import Point

DELIMITERS = (";", "\t")
GENERATED_COLUMN = "Kolumna"


class TableFileError(Exception):
    ...


@dataclass
class Table:
    columns: list[str]
    rows: list[list[str]]

    def to_points(self, x_index: int, y_index: int) -> list[Point]:
        points: list[Point] = []

        for number, row in enumerate(self.rows, start=1):
            points.append(
                Point(
                    _number(row, x_index, self.columns[x_index], number),
                    _number(row, y_index, self.columns[y_index], number),
                )
            )

        return points


def read_table(path: str | Path) -> Table:
    try:
        # utf-8-sig obcina BOM, który dopisują Notatnik, Excel i PowerShell.
        content = Path(path).read_text(encoding="utf-8-sig")
    except OSError as error:
        raise TableFileError(f"Nie można odczytać pliku: {error}") from error
    except UnicodeDecodeError as error:
        raise TableFileError("Plik nie jest tekstem w kodowaniu UTF-8.") from error

    lines = [line.strip() for line in content.splitlines() if line.strip()]
    lines = [line for line in lines if not line.startswith("#")]

    if not lines:
        raise TableFileError("Plik nie zawiera żadnych danych.")

    delimiter = _delimiter(lines[0])
    rows = [_split(line, delimiter) for line in lines]

    if _is_header(rows[0]):
        columns = rows.pop(0)
    else:
        columns = [f"{GENERATED_COLUMN} {index + 1}" for index in range(len(rows[0]))]

    if len(columns) < 2:
        raise TableFileError("Tabela ma mniej niż dwie kolumny.")

    return Table(columns, rows)


def _delimiter(line: str) -> str | None:
    for delimiter in DELIMITERS:
        if delimiter in line:
            return delimiter

    parts = line.split()
    if len(parts) >= 2 and all(_is_number(part) for part in parts):
        return None

    return "," if "," in line else None


def _split(line: str, delimiter: str | None) -> list[str]:
    if delimiter is None:
        return line.split()

    return [cell.strip() for cell in line.split(delimiter)]


def _is_header(row: list[str]) -> bool:
    return not any(_is_number(cell) for cell in row)


def _is_number(cell: str) -> bool:
    try:
        float(cell.replace(",", "."))
    except ValueError:
        return False

    return True


def _number(row: list[str], index: int, name: str, number: int) -> float:
    if index >= len(row):
        raise TableFileError(f'Wiersz {number}: brak kolumny "{name}".')

    try:
        return float(row[index].replace(",", "."))
    except ValueError as error:
        raise TableFileError(
            f'Wiersz {number}: kolumna "{name}" ma wartość "{row[index]}", która nie jest liczbą.'
        ) from error
