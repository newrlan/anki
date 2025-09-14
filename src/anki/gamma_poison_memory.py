from dataclasses import dataclass
from typing import Any, List

from numpy import sqrt
from anki.prototypes import Memory
import pandas as pd

# NOTE: выбрал архитектуру в функциональном стиле. Код получится немного
# громоздким из-за большого количества входных параметров, но зато его можно
# будет применять через apply

def gamma_poison_update(
    mu: float,
    dispersion: float,
    success: int,   # сколько раз не вспомнил слово
    total: int,     # сколько раз слово было показано
    eta: float = 1,
):

    # В redme описаны формулы через ср.кв.отклонение, но для вычислений удобнее
    # работать с дисперсией d = s**2

    # TODO: перейти от sigma к dispersion

    gamma_t = mu / dispersion
    gamma_tt = gamma_t + total
    mu_tt = (mu * gamma_t + success) / gamma_tt
    dispersion_tt = mu_tt / gamma_tt

    new_dispersion = dispersion_tt + eta * (mu_tt ** 2 + dispersion_tt)
    return mu_tt, new_dispersion


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

