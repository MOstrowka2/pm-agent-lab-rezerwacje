"""Model danych rezerwacji stanowisk (WORK-01)."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Slot:
    """Przedział czasu rezerwacji [start, end)."""

    start: datetime
    end: datetime

    def __post_init__(self) -> None:
        if self.end <= self.start:
            raise ValueError("koniec przedziału musi być po jego początku")

    def overlaps(self, other: Slot) -> bool:
        """Przedziały stykające się końcami nie kolidują."""
        return self.start < other.end and other.start < self.end


@dataclass
class Desk:
    desk_id: str
    available: bool = True


@dataclass(frozen=True)
class Reservation:
    reservation_id: str
    desk_id: str
    owner: str
    slot: Slot
