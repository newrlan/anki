from dataclasses import dataclass, field
from typing import List
from uuid import uuid4


@dataclass
class Word:
    word: str
    context: List[str]
    translation: List[str]
    id: str = field(default_factory=lambda: str(uuid4()))

    def __repr__(self):
        return f"{self.word} / {' ,'.join(self.translation)}"
