class Jugador:
    def __init__(self, ficha:str, nombre:str):
        self.ficha = ficha
        self.nombre = nombre
        self.estado = "Jugando"
    
    # setters
    def cambiarEstado(self, nuevoEstado:str):
        self.estado = nuevoEstado