import unittest
from gestion_dispositivos import agregar_dispositivo, listar_dispositivos, actualizar_dispositivo, eliminar_dispositivo

class TestGestionDispositivos(unittest.TestCase):

    def test_agregar_dispositivo(self):
        data = {"name": "Switch 2", "type": "Switch", "status": "active"}
        result = agregar_dispositivo(data)
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Switch 2")

    def test_listar_dispositivos(self):
        result = listar_dispositivos()
        self.assertIsNotNone(result)
        self.assertTrue(len(result) > 0)

    def test_actualizar_dispositivo(self):
        data = {"name": "Router 1 Actualizado", "type": "Router", "status": "inactive"}
        result = actualizar_dispositivo(1, data)
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Router 1 Actualizado")

    def test_eliminar_dispositivo(self):
        result = eliminar_dispositivo(2)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
