from jugador import Jugador
from tablero import Tablero

class Tateti:
    def __init__(self, jugadorX: Jugador, jugadorO: Jugador):
        self.turno = "X"
        self.tablero = Tablero()
        self.jugadorX = jugadorX
        self.jugadorO = jugadorO
        self.estado = "Activo"
    
    def ocuparCasilla(self, fila: int, columna: int):
        self.tablero.ponerFicha(self.turno, fila, columna)
        # Cambiar turno
        if self.turno == "X":
            self.turno = "O"
        else:
            self.turno = "X"
    
    def evaluarGanador(self):
        t = self.tablero.contenedor
        # verifica las filas
        for fila in t:
            if fila[0] == fila[1] == fila[2] != "":
                return fila[0]
        # verifica las columnas
        for columna in range(3):
            if t[0][columna] == t[1][columna] == t[2][columna] != "":
                return t[0][columna]
        # verivica las diagonales
        if t[0][0] == t[1][1] == t[2][2] != "":
            return t[0][0]
        if t[0][2] == t[1][1] == t[2][0] != "":
            return t[0][2]
        return None  # Sin ganador
    
    def evaluarEmpate(self):
        return self.tablero.lleno and self.evaluarGanador() is None
