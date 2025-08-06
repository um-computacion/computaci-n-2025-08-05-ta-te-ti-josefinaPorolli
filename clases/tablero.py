# Excepción
def posicionOcupadaException(Exception):
    pass

class Tablero:
    def __init__(self):
        self.contenedor = [["", "", ""],
                           ["", "", ""],
                           ["", "", ""]]
        self.lleno = False # este atributo determina si se ocuparon todas las posiciones del tablero.
    
    # setters
    def marcarComoLleno(self):
        self.lleno = True

    def ponerFicha(self, ficha, fila, columna):
        if self.contenedor[fila][columna] == "":
            self.contenedor[fila][columna] == ficha
        else:
            raise posicionOcupadaException("¡Posición ocupada! Elegí otra posición.")
