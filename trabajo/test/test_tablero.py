import unittest
from src.handlers import tablero


# Diego Lanciotti - test actividad adicional
class TestFuncionProcesarLogos(unittest.TestCase):

    def test_procesar_logos_estructura(self):
        """ Testea que la funcion procesar_logos devuelva la estructura correcta"""
        self.assertTrue(isinstance(tablero.procesar_logos(), list))  # Tipo lista
        self.assertTrue(isinstance(tablero.procesar_logos()[0], list))  # Tipo lista de lista
        self.assertEqual(len(tablero.procesar_logos()[0]), 2)  # Tamaño 2 [nombre, imagen]
        self.assertTrue(isinstance(tablero.procesar_logos()[0], list))
        self.assertTrue(isinstance(tablero.procesar_logos()[0], list))

    def test_procesar_logos_modos(self):
        """ Testea que la funcion procesar_logos reciba el parametro modo"""
        self.assertNotEqual(tablero.procesar_logos(modo=1), tablero.procesar_logos(modo=2))  # Distintos datos
        self.assertEqual(tablero.procesar_logos(), tablero.procesar_logos(modo=1))  # Iguales datos


if __name__ == '__main__':
    unittest.main()
