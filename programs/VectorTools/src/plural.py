"""Odmiana rzeczowników po liczbie."""


def plural(count: int, one: str, few: str, many: str) -> str:
    if count == 1:
        return one
    if 2 <= count % 10 <= 4 and not 12 <= count % 100 <= 14:
        return few
    return many
