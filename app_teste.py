import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
  
 def setUp(self):
   self.client = app.test_client()

 def test_devops(self):
   response = self.client.get('/')
   self.assertEqual(response.status_code, 200)
   self.assertIn(b'Germinare',response.data)

  def test_murilo(self):
   response = self.client.get('/Murilo')
   self.assertEqual(response.status_code, 200)
   self.assertIn(b'MURILO',response.data)

if __name__ == '__main__':
 unittest.main()
