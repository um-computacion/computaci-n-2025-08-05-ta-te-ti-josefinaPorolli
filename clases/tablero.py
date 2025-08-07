# Excepción
def posicionOcupadaException(Exception):
    pass

class Tablero:
    def __init__(self):
        self.contenedor = [["", "", ""],
                           ["", "", ""],
                           ["", "", ""]]
        self.lleno = False  # Determina si todas las posiciones están ocupadas.
    
    def ponerFicha(self, ficha: str, fila: int, columna: int):
        if self.contenedor[fila][columna] == "":
            self.contenedor[fila][columna] = ficha
            # Chequea si quedó lleno
            if all(c != "" for fila in self.contenedor for c in fila):
                self.lleno = True
        else:
            raise posicionOcupadaException("¡Posición ocupada! Elegí otra posición.")
