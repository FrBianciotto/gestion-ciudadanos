from src.models import Persona

def main():
    persona = Persona(
        dni="12345678", 
        nombre="Juan", 
        apellido="Pérez", 
        edad=19
    )
    
    persona.edad = 20  # tiene que dar error porque la clase es inmutable (frozen=True)
    print(persona)

if __name__ == "__main__":
    main()