# Desafío de Ingeniería - Gestión de Ciudadanos

Solución al desafío técnico de procesamiento de datos de ciudadanos provenientes de un sistema legacy.

## Funcionalidades

El sistema permite:

- Crear personas inmutables.
- Validar que la edad no sea negativa.
- Validar que DNI, nombre y apellido no estén vacíos.
- Evitar DNI duplicados.
- Formatear los registros como un diccionario.
- Obtener la persona de mayor y menor edad.
- Segmentar personas según un umbral de edad.
- Calcular el promedio de edad.
- Consultar la edad de una persona por DNI.

## Estructura del proyecto

gestion-ciudadanos/
├── src/
│   ├── __init__.py
│   ├── models.py
│   └── registro.py
├── tests/
│   ├── __init__.py
│   ├── test_persona.py
│   └── test_registro_personas.py
├── main.py
└── README.md