import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from clases.jugador import Jugador
   

class TestJugador(unittest.TestCase):

    def setUp(self):
        self.jugador = Jugador("X", "Pepito")

    def test_nombre(self):
        self.assertEqual(self.jugador.getNombre(), "Pepito")

    def test_ficha(self):
        self.assertEqual(self.jugador.getFicha(), "X")

if __name__ == '__main__':
    unittest.main()
