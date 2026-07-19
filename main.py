from src.registro import RegistroPersonas

def main():
    datos = [
        ("12345678", "Juan", "Pérez", 19),
        ("87654321", "María", "Gómez", 35), 
        ("11223344", "Carlos", "López", 30)
    ]
    
    registro = RegistroPersonas(datos)
    print(registro.obtener_registros_formateados())

    print("Persona mayor:", registro.obtener_persona_mayor())
    print("Persona menor:", registro.obtener_persona_menor())

    mayores, menores = registro.segmentar_por_edad()

    print("Mayores o iguales al umbral:", mayores)
    print("Menores al umbral:", menores)

if __name__ == "__main__":
    main()