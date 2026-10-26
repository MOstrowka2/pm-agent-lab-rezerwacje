"""Eksperyment: rezerwacje cykliczne (poza zakresem DEC-001)."""

from __future__ import annotations

from datetime import timedelta

from lab_rezerwacje.model import Slot


def weekly(first: Slot, weeks: int) -> list[Slot]:
    """Kolejne tygodniowe powtórzenia przedziału."""
    return [Slot(first.start + timedelta(weeks=i), first.end + timedelta(weeks=i)) for i in range(weeks)]
