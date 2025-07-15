import unittest
from main import app  # assuming your Flask app is in main.py as 'app'

class RoboticArmAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_move_up(self):
        response = self.app.post('/arm/move/up')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Moving up', response.data)  # Adjust based on your actual response

    def test_grab(self):
        response = self.app.post('/arm/grab')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Grabbing', response.data)  # Adjust based on your actual response

if __name__ == '__main__':
    unittest.main()
