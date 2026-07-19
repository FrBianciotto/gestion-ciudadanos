from src.models import Persona

class RegistroPersonas:
    def __init__(self, registros: list[tuple[str, str, str, int]] = None):
        self._personas_por_dni: dict[str, Persona]={}
        
        for dni, nombre, apellido, edad in registros:
            if dni in self._personas_por_dni:
                raise ValueError(f"DNI duplicado: {dni}")

            self._personas_por_dni[dni] = Persona(
                dni=dni,
                nombre=nombre,
                apellido=apellido,
                edad=edad,
            )

    def obtener_registros_formateados(self) -> dict[str, tuple[str, str, int]]:
        return {
            dni: (persona.nombre, persona.apellido, persona.edad)
            for dni, persona in self._personas_por_dni.items()
        }
    
    def obtener_persona_mayor(self) -> Persona:
        if not self._personas_por_dni:
            raise ValueError("No hay personas registradas.")
        
        return max(
            self._personas_por_dni.values(), 
            key=lambda persona: persona.edad
        )
    
    def obtener_persona_menor(self) -> Persona:
        if not self._personas_por_dni:
            raise ValueError("No hay personas registradas.")
        
        return min(
            self._personas_por_dni.values(), 
            key=lambda persona: persona.edad
        )
    
    def segmentar_por_edad(self, umbral: int = 25) -> tuple[list[Persona], list[Persona]]:
        if umbral < 0:
            raise ValueError("El umbral no puede ser negativo.")
        
        mayores_a_umbral = []
        menores_que_umbral = []
        
        for persona in self._personas_por_dni.values():
            if persona.edad >= umbral:
                mayores_a_umbral.append(persona)
            else:
                menores_que_umbral.append(persona)
        
        return mayores_a_umbral, menores_que_umbral
        