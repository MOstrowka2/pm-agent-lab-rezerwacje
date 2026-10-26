"""Rezerwacja stanowiska bez kolizji (REQ-001)."""

from __future__ import annotations

import itertools

from lab_rezerwacje.model import Desk, Reservation, Slot


class Conflict(Exception):
    """Przedział koliduje z istniejącą rezerwacją stanowiska (REQ-001 AC-1)."""


class Unavailable(Exception):
    """Stanowisko jest wyłączone z rezerwacji."""


class ReservationBook:
    def __init__(self, desks: list[Desk]) -> None:
        self.desks = {desk.desk_id: desk for desk in desks}
        self.reservations: list[Reservation] = []
        self._ids = itertools.count(1)

    def reserve(self, desk_id: str, owner: str, slot: Slot) -> Reservation:
        desk = self.desks[desk_id]
        if not desk.available:
            raise Unavailable(desk_id)
        for existing in self.reservations:
            if existing.desk_id == desk_id and existing.slot.overlaps(slot):
                raise Conflict(f"{desk_id}: {existing.reservation_id}")
        reservation = Reservation(f"R-{next(self._ids)}", desk_id, owner, slot)
        self.reservations.append(reservation)
        return reservation


import threading

_LOCK = threading.Lock()


def reserve_safely(book: ReservationBook, desk_id: str, owner: str, slot: Slot) -> Reservation:
    """Równoległe żądania tego samego stanowiska: jedno przyjęte, drugie odrzucone (AC-2)."""
    with _LOCK:
        return book.reserve(desk_id, owner, slot)

# przebieg scenariusza eaedff

# przebieg scenariusza d95159
