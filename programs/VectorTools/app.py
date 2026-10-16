"""Punkt wejścia aplikacji VectorTools."""

from src.layer_indicator import LayerIndicator
from src.layer_store import LayerStore
from src.menu import Menu
from src.menu_operations.close_program import CloseProgram
from src.menu_operations.load_file import LoadFile
from src.menu_operations.load_layer import LoadLayer
from src.menu_operations.show_layer import ShowLayer
from src.menu_operations.show_layer_info import ShowLayerInfo
from src.status_bar import StatusBar
from src.window import MainWindow


def main() -> None:
    window = MainWindow()
    status_bar = StatusBar(window.canvas)
    store = LayerStore()
    indicator = LayerIndicator(window.canvas, store)

    menu = Menu(window.canvas)
    menu.add_option("Wczytaj warstwę", LoadLayer(store, indicator, status_bar))
    menu.add_option("Wyświetl warstwę", ShowLayer(store, status_bar))
    menu.add_option("Wyświetl informacje o warstwie", ShowLayerInfo(store))
    menu.add_option("Wczytaj plik z punktami", LoadFile(window.root, status_bar))
    menu.add_option("Zamknij program", CloseProgram(window.root))

    window.add_resize_listener(status_bar.draw)
    window.add_resize_listener(indicator.draw)
    window.add_resize_listener(menu.draw)

    window.run()


if __name__ == "__main__":
    main()
