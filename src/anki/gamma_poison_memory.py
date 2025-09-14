from dataclasses import dataclass
from typing import Any, List
from anki.prototypes import Memory
import pandas as pd


class GammaPoisonMemory:
    """ Организация памяти по Гамма-Пуассоновской модели. """

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.db = pd.read_csv(db_path)

    @staticmethod
    def _probability(gamma: float, mu: float, sigma2: float) -> float:
        """ Генерация вероятности исходя из параметров. """
        ...

    @staticmethod
    def _update(sucess: int, fails: int) -> tuple[float, float, float]:
        """ Обновление параметров распределений. """
        ...

    def take(self, vol: int) -> List[str]:
        ...

    def update(self, word_id: str, success: int, fails: int) -> None:
        ...

    def register(self, word_id: str) -> None:
        ...

