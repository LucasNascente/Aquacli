import pytest
from unittest.mock import patch
from app import AquaCli, buscar_temperatura_local, ajustar_meta_agua


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


@patch('app.requests.get')
def test_integracao_openweather_api(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'main': {'temp': 32.5}
    }

    temperatura = buscar_temperatura_local("Brasilia", "api_key_falsa")

    assert temperatura == 32.5
    assert ajustar_meta_agua(temperatura) == 2500
