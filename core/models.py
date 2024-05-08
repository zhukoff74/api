from typing import NamedTuple


class Invoice(NamedTuple):
    """Счет"""
    id: int
    up: int
    kps: int
    trtype: str

    
