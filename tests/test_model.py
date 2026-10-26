from datetime import datetime

import pytest

from lab_rezerwacje.model import Slot


def at(hour: int) -> datetime:
    return datetime(2026, 11, 3, hour)


def test_slot_needs_its_end_after_its_start():
    with pytest.raises(ValueError):
        Slot(at(10), at(10))


def test_touching_slots_do_not_overlap():
    assert not Slot(at(9), at(10)).overlaps(Slot(at(10), at(11)))
    assert Slot(at(9), at(11)).overlaps(Slot(at(10), at(12)))
