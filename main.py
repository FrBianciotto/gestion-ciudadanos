from src.registro import RegistroPersonas

def main() -> None:
    datos = [
        ("12345678", "Juan", "Pérez", 19),
        ("87654321", "María", "Gómez", 35), 
        ("11223344", "Carlos", "López", 30)
    ]
    
    registro = RegistroPersonas(datos)
    print(registro.obtener_registros_formateados())

    print("\n Persona mayor:", registro.obtener_persona_mayor())
    print("\n Persona menor:", registro.obtener_persona_menor())

    mayores, menores = registro.segmentar_por_edad()

    print("\nMayores o iguales al umbral:", mayores)
    print("\n Menores al umbral:", menores)

    print("\n Promedio de edad:", registro.calcular_promedio_edad())

    print("\n Edad de la persona con DNI 87654321:", registro.obtener_edad_por_dni("87654321"))

if __name__ == "__main__":
    main()