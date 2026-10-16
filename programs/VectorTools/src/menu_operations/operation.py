"""Wspólny interfejs operacji dostępnych z menu."""

from abc import ABC, abstractmethod


class MenuOperation(ABC):
    @abstractmethod
    def execute(self) -> None:
        ...
