import pytest
from app import AquaCli

# 1. Caminho feliz: Testa se a água é adicionada corretamente
def test_add_water_success():
    tracker = AquaCli()
    tracker.add_water(500)
    assert tracker.total_water == 500

# 2. Entrada inválida: Testa se o sistema bloqueia valores negativos
def test_add_water_negative_value():
    tracker = AquaCli()
    with pytest.raises(ValueError):
        tracker.add_water(-100)

# 3. Caso limite: Testa se a mensagem de meta atingida funciona no limite exato
def test_check_status_goal_reached():
    tracker = AquaCli(goal=2000)
    tracker.add_water(2000)
    assert tracker.check_status() == "Parabéns! Você atingiu sua meta diária de hidratação!"