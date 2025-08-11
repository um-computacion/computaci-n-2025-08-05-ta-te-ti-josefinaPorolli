import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from clases.tateti import Tateti
from clases.jugador import Jugador

def main():
    print("¡Bienvenidos al Ta-te-ti!")
    while True:
        nombreX = input("Ingrese el nombre del jugador X: ")
        nombreO = input("Ingrese el nombre del jugador O: ")
        jugadorX = Jugador("X", nombreX)
        jugadorO = Jugador("O", nombreO)
        tateti = Tateti(jugadorX, jugadorO)
        
        while tateti.evaluarEmpate() == False:
            if(tateti.getTurno() == "X"):
                print(f"Turno de {jugadorX.nombre} (X)")
            else:
                print(f"Turno de {jugadorO.nombre} (O)")
            try:
                fila = abs(int(input("Ingrese la fila (1, 2, 3): "))) - 1 # en caso de que el usuario tenga ganas de hacer cualquier cosa, si pone un negativo se toma el valor absoluto :p
                columna = abs(int(input("Ingrese la columna (1, 2, 3): "))) - 1
                tateti.ocuparCasilla(fila, columna)
            # Para números no enteros
            except ValueError:
                print("Entrada inválida. Por favor ingrese números enteros para fila y columna.")
                continue
            # Para números fuera de rango
            except IndexError:
                print("Índice fuera de rango. Por favor ingrese valores entre 1 y 3.")
                continue
            except Exception as e:
                print(e)
                continue

            # mostrar el tablero
            tablero = tateti.tablero.contenedor
            for fila in tablero:
                print(" | ".join(fila))
                print("-" * 9)

            ganador = tateti.evaluarGanador()
            if ganador == "X":
                print(f"¡Felicidades {jugadorX.nombre}! Has ganado el juego.")
                break
            elif ganador == "O":
                print(f"¡Felicidades {jugadorO.nombre}! Has ganado el juego.")
                break
            elif tateti.evaluarEmpate():
                print("¡Es un empate! No hay más movimientos posibles.")
                break

if __name__ == "__main__":
    main()