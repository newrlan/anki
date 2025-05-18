from pathlib import Path
from typing import Self
from word_card import Card
import logging


class Vocabular:
    def __init__(self, storage: Path):
        ...

    @classmethod
    def load(cls, storage: Path) -> Self:
        ...
