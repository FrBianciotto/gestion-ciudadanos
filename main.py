from src.registro import RegistroPersonas

def main():
    datos = [
        ("12345678", "Juan", "Pérez", 19),
        ("87654321", "María", "Gómez", 25), 
        ("11223344", "Carlos", "López", 30)
    ]
    
    registro = RegistroPersonas(datos)
    print(registro.obtener_registros_formateados())

if __name__ == "__main__":
    main()