# Ta-te-ti

## Datos del Alumno

- **Nombre**: Josefina Porolli Serpa
- **Legajo**: 64133
- **Materia**: Computación I
- **Año**: 2025

## Descripción

Este proyecto implementa el clásico juego de Ta-te-ti en Python. El juego permite que dos jugadores compitan entre sí, alternando turnos para colocar sus fichas (X y O) en un tablero 3x3. El juego termina cuando un jugador logra alinear tres de sus fichas en línea recta (horizontal, vertical o diagonal) o cuando el tablero se llena sin un ganador (empate).
La dinámica del juego en el presente programa es la siguiente:

1. Se crea una nueva partida.
2. Se ingresan los nombres de cada jugador, previamente acordando quién es la X y quién es la O.
3. Por reglas del juego, siempre comienza el jugador X.
4. Cada jugador pone primero la fila y luego la columna (1, 2 o 3) para colocar su ficha en el tablero.
5. Gana el jugador que logre poner 3 de sus fichas en línea, ya sea de forma vertical, horizontal o diagonal. Hay un empate en caso de que se llene el tablero y no se haya logrado hacer ninguna línea de 3 fichas.

## Cómo Ejecutar

### Jugar una Partida

Para iniciar el juego, ejecuta el siguiente comando en la terminal:

```bash
python cli.py
```

El juego pedirá los nombres de los jugadores y luego permitirá que cada uno ingrese sus movimientos indicando fila (1-3) y columna (1-3).

### Ejecutar Tests

Para ejecutar todos los tests unitarios, usa cualquiera de estos comandos:

```bash
python -m unittest tests/test_jugador.py
python -m unittest tests/test_tablero.py
python -m unittest tests/test_tateti.py
```
