import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from clases.tablero import Tablero, posicionOcupadaException

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()

    def test_get_vacio(self): # primero prefiero hacer un test para asegurarme de que está vacío (hay espacios sin ocupar)
        self.assertFalse(self.tablero.getLleno())

    def test_poner_ficha(self):
        self.tablero.ponerFicha("X", 0, 0) #pone una x en la esquina superior izquierda
        self.tablero.ponerFicha("O", 1, 0) #pone una o en la segunda fila, primera columna
        self.assertEqual(self.tablero.contenedor[0][0], "X")
        self.assertEqual(self.tablero.contenedor[0][1], "")
        self.assertEqual(self.tablero.contenedor[0][2], "")
        self.assertEqual(self.tablero.contenedor[1][0], "O")
        self.assertEqual(self.tablero.contenedor[1][1], "")
        self.assertEqual(self.tablero.contenedor[1][2], "")
        self.assertEqual(self.tablero.contenedor[2][0], "")
        self.assertEqual(self.tablero.contenedor[2][1], "")
        self.assertEqual(self.tablero.contenedor[2][2], "")

    def test_poner_ficha_en_posicion_ocupada(self):
        self.tablero.ponerFicha("X", 0, 0)
        with self.assertRaises(posicionOcupadaException):
            self.tablero.ponerFicha("O", 0, 0)

    def test_tablero_lleno(self):
        self.tablero.ponerFicha("X", 0, 0)
        self.tablero.ponerFicha("O", 0, 1)
        self.tablero.ponerFicha("O", 0, 2)
        self.tablero.ponerFicha("O", 1, 0)
        self.tablero.ponerFicha("X", 1, 1)
        self.tablero.ponerFicha("X", 1, 2)
        self.tablero.ponerFicha("X", 2, 0)
        self.tablero.ponerFicha("X", 2, 1)
        self.tablero.ponerFicha("O", 2, 2)
        self.assertTrue(self.tablero.getLleno())
5
if __name__ == '__main__':
    unittest.main()
