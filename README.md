# Ahorcado Ágiles

Este proyecto es una implementación en Python del clásico juego del ahorcado, siguiendo prácticas ágiles y pruebas ATDD (Acceptance Test–Driven Development) para garantizar que el comportamiento cumple con los requisitos esperados.

## Integrantes
- Cravero, Pablo - Legajo: 50020;
- Gini, Luca - Legajo: 49497;
- Griva, Corina - Legajo: 49670;
- Gutierrez, Luisina - Legajo: 49742;
- Pérez Fontela, Simón - Legajo: 50180.

## Requisitos

- Python 3.x instalado en tu máquina.
- Dependencias (si existen en `requirements.txt`):
  ```bash
  pip install -r requirements.txt
  ```
  En caso contrario, puedes instalar manualmente las herramientas necesarias:
  ```bash
  pip install behave pytest coverage flake8 
  ```

## Ejecución

### 1. ATDD con Behave

Para ejecutar los escenarios de aceptación definidos en `features/`:
```bash
behave
```

### 2. Ejecución local de la aplicación

Para iniciar la aplicación y jugar localmente:
```bash
python app.py
```

### 3. Pruebas unitarias

Para ejecutar los tests de unidad:
```bash
python test_ahorcado.py
```

## Estructura del proyecto

- `features/`      Carpeta con escenarios de ATDD para Behave.  
- `app.py`         Punto de entrada de la aplicación.  
- `test_ahorcado.py` Tests unitarios para la lógica del juego.
