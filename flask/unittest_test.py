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
        self.assertIn(b'a30ee592b51f2f382a1e9d2dd0baed8920e8d51a', response.data)
    
    def test_post(self):
        response = self.app.post('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'a30ee592b51f2f382a1e9d2dd0baed8920e8d51a', response.data)

    # executed after each test
    def tearDown(self):
        pass
 
if __name__ == "__main__":
    unittest.main()