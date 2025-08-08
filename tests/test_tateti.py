import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from clases.tateti import Tateti
from clases.jugador import Jugador
from clases.tablero import Tablero

class TestTateti(unittest.TestCase):

    def setUp(self):
        self.jugador1 = Jugador("X", "Pablito")
        self.jugador2 = Jugador("O", "Clavounclavito")
        self.tateti = Tateti(self.jugador1, self.jugador2)

    def test_parametros_iniciales(self):
        self.assertEqual(self.tateti.getTurno(), "X")
        self.assertEqual(self.tateti.tablero.contenedor, [["", "", ""], ["", "", ""], ["", "", ""]])

    def test_ocupar_casilla(self):
        self.assertEqual(self.tateti.getTurno(), "X")
        self.tateti.ocuparCasilla(0, 0)
        self.assertEqual(self.tateti.tablero.contenedor[0][0], "X")
        self.assertEqual(self.tateti.getTurno(), "O")
        self.tateti.ocuparCasilla(1, 1)
        self.assertEqual(self.tateti.tablero.contenedor[1][1], "O")

    def test_evaluar_ganador(self):
        self.tateti.ocuparCasilla(0, 0) # X
        self.tateti.ocuparCasilla(2, 1) # O
        self.tateti.ocuparCasilla(0, 2) # X
        self.tateti.ocuparCasilla(1, 1) # O
        self.tateti.ocuparCasilla(0, 1) # X
        self.assertEqual(self.tateti.evaluarGanador(), "X") # Ganaría la X
    
    def test_evaluar_empate(self):
        self.tateti.ocuparCasilla(0, 0) # X
        self.tateti.ocuparCasilla(0, 1) # O
        self.tateti.ocuparCasilla(1, 1) # X
        self.tateti.ocuparCasilla(0, 2) # O
        self.tateti.ocuparCasilla(1, 2) # X
        self.tateti.ocuparCasilla(1, 0) # O
        self.tateti.ocuparCasilla(2, 0) # X
        self.tateti.ocuparCasilla(2, 2) # O
        self.tateti.ocuparCasilla(2, 1) # X
        self.assertIsNone(self.tateti.evaluarGanador())
        self.assertTrue(self.tateti.evaluarEmpate())

if __name__ == '__main__':
    unittest.main()