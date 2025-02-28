from pathlib import Path
from typing import Self
from word_card import Card
import logging


IGR = 0.618         # обратное золотое сечение
DEFAULT_FORGOT = 1  # время забывания в минутах


class Vocabular:
    def __init__(self, storage: Path):
        ...

    @classmethod
    def load(cls, storage: Path) -> Self:
        ...

