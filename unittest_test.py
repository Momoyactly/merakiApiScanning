import unittest
from app import create_app

class BasicTests(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_get(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # executed after each test
    def tearDown(self):
        pass
 
if __name__ == "__main__":
    unittest.main()