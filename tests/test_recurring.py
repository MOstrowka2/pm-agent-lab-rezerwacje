from datetime import datetime

from lab_rezerwacje.model import Slot
from lab_rezerwacje.recurring import weekly


def test_weekly_repeats_the_slot():
    slots = weekly(Slot(datetime(2026, 11, 3, 9), datetime(2026, 11, 3, 10)), 3)
    assert [s.start.day for s in slots] == [3, 10, 17]
