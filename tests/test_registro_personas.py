import pytest

from src.registro import RegistroPersonas
from src.models import Persona

def test_creacion_registro_personas_valida() -> None:
    datos = [
        ("12345678", "Juan", "Pérez", 19),
        ("87654321", "María", "Gómez", 35), 
        ("11223344", "Carlos", "López", 30)
    ]
    
    registro = RegistroPersonas(datos)
    
    registros_formateados = registro.obtener_registros_formateados()
    
    assert len(registros_formateados) == 3
    assert registros_formateados["12345678"] == ("Juan", "Pérez", 19)
    assert registros_formateados["87654321"] == ("María", "Gómez", 35)
    assert registros_formateados["11223344"] == ("Carlos", "López", 30)

def test_creacion_registro_personas_con_dni_duplicado() -> None:
    datos = [
        ("12345678", "Juan", "Pérez", 19),
        ("12345678", "María", "Gómez", 35), 
    ]
    
    with pytest.raises(ValueError):
        RegistroPersonas(datos)

def test_obtener_persona_mayor_y_menor() -> None:
    datos = [
        ("12345678", "Juan", "Pérez", 19),
        ("87654321", "María", "Gómez", 35), 
        ("11223344", "Carlos", "López", 30)
    ]
    
    registro = RegistroPersonas(datos)
    
    persona_mayor = registro.obtener_persona_mayor()
    persona_menor = registro.obtener_persona_menor()
    
    assert persona_mayor == Persona("87654321", "María", "Gómez", 35)
    assert persona_menor == Persona("12345678", "Juan", "Pérez", 19)

def test_segmentar_por_edad() -> None:
    datos = [
        ("12345678", "Juan", "Pérez", 19),
        ("87654321", "María", "Gómez", 35), 
        ("11223344", "Carlos", "López", 25)
    ]
    
    registro = RegistroPersonas(datos)
    
    mayores, menores = registro.segmentar_por_edad(25)
    
    assert mayores == [
        Persona("87654321", "María", "Gómez", 35),
        Persona("11223344", "Carlos", "López", 25),
    ]

    assert menores == [
        Persona("12345678", "Juan", "Pérez", 19),
    ]

def test_calcular_promedio_edad() -> None:
    datos = [
        ("12345678", "Juan", "Pérez", 19),
        ("87654321", "María", "Gómez", 35), 
        ("11223344", "Carlos", "López", 30)
    ]
    
    registro = RegistroPersonas(datos)
    
    promedio_edad = registro.calcular_promedio_edad()
    
    assert promedio_edad == pytest.approx((19 + 35 + 30) / 3)

def test_obtener_edad_por_dni() -> None:
    datos = [
        ("12345678", "Juan", "Pérez", 19),
        ("87654321", "María", "Gómez", 35), 
        ("11223344", "Carlos", "López", 30)
    ]
    
    registro = RegistroPersonas(datos)
    
    edad_juan = registro.obtener_edad_por_dni("12345678")
    edad_maria = registro.obtener_edad_por_dni("87654321")
    
    assert edad_juan == 19
    assert edad_maria == 35
    
    with pytest.raises(ValueError):
        registro.obtener_edad_por_dni("00000000") 

def test_segmentar_por_edad_con_umbral_negativo() -> None:
    datos = [
        ("12345678", "Juan", "Pérez", 19),
        ("87654321", "María", "Gómez", 35), 
        ("11223344", "Carlos", "López", 30)
    ]
    
    registro = RegistroPersonas(datos)
    
    with pytest.raises(ValueError):
        registro.segmentar_por_edad(-5)

def test_extremos_y_promedio_sin_registros() -> None:
    registro = RegistroPersonas([])
    
    with pytest.raises(ValueError):
        registro.obtener_persona_mayor()
    
    with pytest.raises(ValueError):
        registro.obtener_persona_menor()
    
    with pytest.raises(ValueError):
        registro.calcular_promedio_edad()
  