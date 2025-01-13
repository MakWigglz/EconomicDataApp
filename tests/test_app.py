import unittest
from app import app
from app.utils import init_db, populate_db

class TestEconomicDataApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        self.db = init_db()
        populate_db(self.db)

    def tearDown(self):
        self.db.close()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Economic Indicators Dashboard', response.data)

    def test_get_data_route(self):
        response = self.app.get('/data/GDP Growth')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn('plot_url', json_data)
        self.assertIn('data', json_data)

    def test_indicators_exist(self):
        response = self.app.get('/')
        self.assertIn(b'GDP Growth', response.data)
        self.assertIn(b'Inflation Rate', response.data)
        self.assertIn(b'Unemployment Rate', response.data)

    def test_invalid_indicator(self):
        response = self.app.get('/data/InvalidIndicator')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()