from datetime import datetime

import pytest

from lab_rezerwacje.booking import Conflict, ReservationBook
from lab_rezerwacje.model import Desk, Slot


def slot(start: int, end: int) -> Slot:
    return Slot(datetime(2026, 11, 3, start), datetime(2026, 11, 3, end))


def test_a_conflicting_reservation_is_refused():  # REQ-001 AC-1
    book = ReservationBook([Desk("D1")])
    book.reserve("D1", "anna", slot(9, 11))
    with pytest.raises(Conflict):
        book.reserve("D1", "jan", slot(10, 12))


def test_non_overlapping_reservations_are_accepted():  # REQ-001 AC-3
    book = ReservationBook([Desk("D1")])
    book.reserve("D1", "anna", slot(9, 10))
    book.reserve("D1", "jan", slot(10, 11))
    assert len(book.reservations) == 2
