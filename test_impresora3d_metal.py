import pytest
from impresora3dmetal import Impresora3DMetal

@pytest.mark.parametrize("input_temp, expected", [
    (500, 500),
    (1000, 1000),
    (0, 0)
])
def test_temperatura_valida(input_temp, expected):
    impresora = Impresora3DMetal()
    impresora.set_temperatura(input_temp)
    assert impresora.get_temperatura() == expected

@pytest.mark.parametrize("input_temp", [
    1600, -100, 2000
])
def test_temperatura_invalida(input_temp):
    impresora = Impresora3DMetal()
    with pytest.raises(ValueError):
        impresora.set_temperatura(input_temp)

@pytest.mark.parametrize("input_speed, expected", [
    (1, 1),
    (5, 5),
    (10, 10)
])
def test_velocidad_valida(input_speed, expected):
    impresora = Impresora3DMetal()
    impresora.set_velocidad_impresion(input_speed)
    assert impresora.get_velocidad_impresion() == expected

@pytest.mark.parametrize("input_speed", [
    0, 11, 15
])
def test_velocidad_invalida(input_speed):
    impresora = Impresora3DMetal()
    assert impresora.ajustar_velocidad(input_speed) is None

@pytest.mark.parametrize("input_level, expected", [
    (0, 0),
    (50, 50),
    (100, 100)
])
def test_nivel_polvo_valido(input_level, expected):
    impresora = Impresora3DMetal()
    impresora.set_nivel_polvo_metal(input_level)
    assert impresora.get_nivel_polvo_metal() == expected

@pytest.mark.parametrize("input_level", [
    -10, 110, 200
])
def test_nivel_polvo_invalido(input_level):
    impresora = Impresora3DMetal()
    with pytest.raises(ValueError):
        impresora.set_nivel_polvo_metal(input_level)

@pytest.mark.parametrize("initial_temp, increment, expected", [
    (0, 200, 200),
    (500, 600, 1100),
    (1400, 200, 1500),
])
def test_calentar(initial_temp, increment, expected):
    impresora = Impresora3DMetal()
    impresora.set_temperatura(initial_temp)
    assert impresora.calentar(increment) == expected

@pytest.mark.parametrize("initial_level, speed, tiempo, expected_level", [
    (100, 5, 100, 50),
    (50, 2, 100, 30),
])
def test_imprimir_con_exito(initial_level, speed, tiempo, expected_level):
    impresora = Impresora3DMetal()
    impresora.set_velocidad_impresion(speed)
    impresora.set_nivel_polvo_metal(initial_level)
    resultado = impresora.imprimir(tiempo)
    assert resultado == expected_level

@pytest.mark.parametrize("initial_level, speed, tiempo", [
    (10, 5, 1000),
    (0, 10, 100),
])
def test_imprimir_fallo(initial_level, speed, tiempo):
    impresora = Impresora3DMetal()
    impresora.set_velocidad_impresion(speed)
    impresora.set_nivel_polvo_metal(initial_level)
    assert impresora.imprimir(tiempo) is None
