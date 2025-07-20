from typing import Any, List, Protocol, runtime_checkable


@runtime_checkable
class Memory(Protocol):
    def take(self, vol: int) -> List[Any]:
        ...

    def update(self, word_id: Any, success: int, fail: int) -> None:
        ...

    def register(self, word_id: Any) -> None:
        ...
