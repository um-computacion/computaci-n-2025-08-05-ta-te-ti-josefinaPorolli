class Jugador:
    def __init__(self, ficha:str, nombre:str):
        self.ficha = ficha
        self.nombre = nombre
    
    # getters
    def getNombre(self):
        return self.nombre
    def getFicha(self):
        return self.ficha