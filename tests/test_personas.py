from dataclasses import FrozenInstanceError

import pytest

from src.models import Persona

def test_creacion_persona_valida() -> None:
    persona = Persona(
        dni="12345678", 
        nombre="Juan", 
        apellido="Pérez", 
        edad=30
        )
    
    assert persona.dni == "12345678"
    assert persona.nombre == "Juan"
    assert persona.apellido == "Pérez"
    assert persona.edad == 30

def test_creacion_persona_con_datos_invalidos() -> None:
    with pytest.raises(ValueError):
        Persona(
            dni="", 
            nombre="Juan", 
            apellido="Pérez", 
            edad=30)
    
    with pytest.raises(ValueError):
        Persona(
            dni="12345678", 
            nombre="", 
            apellido="Pérez", 
            edad=30)
    
    with pytest.raises(ValueError):
        Persona(
            dni="12345678", 
            nombre="Juan", 
            apellido="", 
            edad=30)
    
    with pytest.raises(ValueError):
        Persona(
            dni="12345678", 
            nombre="Juan", 
            apellido="Pérez", 
            edad=-5)
        
def test_persona_inmutable() -> None:
    persona = Persona(
        dni="12345678", 
        nombre="Juan", 
        apellido="Pérez", 
        edad=30
        )
    
    with pytest.raises(FrozenInstanceError):
        persona.nombre = "Carlos"
    
    with pytest.raises(FrozenInstanceError):
        persona.edad = 35