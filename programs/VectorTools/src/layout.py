"""Przeliczanie układu z rozmiaru projektowego na aktualny rozmiar okna."""

from src import config


def scaled(position: tuple[int, int], size: tuple[int, int]) -> tuple[int, int]:
    width, height = size

    return (
        round(position[0] * width / config.WINDOW_WIDTH),
        round(position[1] * height / config.WINDOW_HEIGHT),
    )


def scaled_font(font: tuple[str, int, str], size: tuple[int, int]) -> tuple[str, int, str]:
    width, height = size
    ratio = min(width / config.WINDOW_WIDTH, height / config.WINDOW_HEIGHT)

    family, points, style = font

    return (family, max(1, round(points * ratio)), style)
