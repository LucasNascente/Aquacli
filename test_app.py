import pytest
from app import AquaCli


def test_add_water_success():
    tracker = AquaCli()
    tracker.add_water(500)
    assert tracker.total_water == 500


def test_add_water_negative_value():
    tracker = AquaCli()
    with pytest.raises(ValueError):
        tracker.add_water(-100)


def test_check_status_goal_reached():
    tracker = AquaCli(goal=2000)
    tracker.add_water(2000)
    msg = "Parabéns! Você atingiu sua meta diária!"
    assert tracker.check_status() == msg

