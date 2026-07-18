from dataclasses import dataclass

@dataclass(frozen=True)
class Persona:
    dni: str
    nombre: str
    apellido: str
    edad: int

    def __post_init__(self):
        if not self.dni or not self.nombre or not self.apellido:
            raise ValueError("DNI, nombre y apellido no pueden estar vacíos.")
        if self.edad < 0:
            raise ValueError("La edad no puede ser negativa.")