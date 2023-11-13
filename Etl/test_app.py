import unittest
from app import app

class ETLTest(unittest.TestCase):

    def test_extract_transform_load(self):
        tester = app.test_client(self)
        response = tester.get('/extract_transform_load')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.json, {'message': 'ETL executado com sucesso!'})

if __name__ == '__main__':
    unittest.main()
