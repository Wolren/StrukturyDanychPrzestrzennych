"""Konfiguracja wyglądu aplikacji VectorTools."""

from pathlib import Path

TITLE = "VectorTools"

WINDOW_WIDTH = 650
WINDOW_HEIGHT = 550

WINDOW_MIN_WIDTH = 400
WINDOW_MIN_HEIGHT = 350

RESIZE_DELAY = 60

BACKGROUND_IMAGE = Path(__file__).parent / "img" / "wiewior.jpg"
BACKGROUND_PLACEHOLDER_COLOR = "#012A4A"

FONT_FAMILY = "Consolas"

TEXT_COLOR = "white"
TEXT_HOVER_COLOR = "#90E0EF"

TITLE_FONT = (FONT_FAMILY, 30, "bold")
HEADING_FONT = (FONT_FAMILY, 16, "bold")
OPTION_FONT = (FONT_FAMILY, 11, "bold")

TITLE_POSITION = (200, 50)

MENU_X = 180
MENU_HEADING = "Wybierz operację:"
MENU_HEADING_POSITION = (MENU_X, 310)
MENU_FIRST_OPTION_Y = 350
MENU_OPTION_SPACING = 35

LAYER_STATUS_TEXT = "PLIK ZAŁADOWANY PRAWIDŁOWO"
LAYER_STATUS_POSITION = (MENU_X, 275)
LAYER_STATUS_FONT = (FONT_FAMILY, 11, "bold")
LAYER_STATUS_COLOR = "#3DFF7A"
LAYER_STATUS_TAG = "layer_status"

STATUS_POSITION = (20, 535)
STATUS_FONT = (FONT_FAMILY, 9, "bold")

FILE_DIALOG_TITLE = "Wybierz plik z punktami"
FILE_DIALOG_TYPES = [
    ("Pliki z danymi", "*.txt *.csv *.dat"),
    ("Wszystkie pliki", "*.*"),
]

COLUMN_DIALOG_TITLE = "Wskaż kolumny ze współrzędnymi"

LAYER_DIALOG_TITLE = "Wybierz warstwę"
LAYER_DIALOG_TYPES = [
    ("Pliki GIS", "*.shp *.geojson *.json *.gpkg *.kml"),
    ("Wszystkie pliki", "*.*"),
]

LAYER_COLOR_COLUMN = "legenda"
LAYER_COLORMAP = "tab10"
