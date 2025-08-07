class Jugador:
    def __init__(self, ficha:str, nombre:str):
        self.ficha = ficha
        self.nombre = nombre
        self.estado = "Jugando"
    
    # setters
    def cambiarEstado(self, nuevoEstado:str):
        self.estado = nuevoEstado
    def setNombre(self, nombre:str):
        self.nombre = nombre
    # getters
    def getNombre(self):
        return self.nombre
    def getFicha(self):
        return self.ficha