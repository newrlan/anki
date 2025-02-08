from dataclasses import dataclass
from typing import List


@dataclass
class WordCard:
    word: str
    context: List[str]
    translation: List[str]
