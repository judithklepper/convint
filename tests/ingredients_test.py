import unittest
import requests


class TestIngredientsService(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5001/stocks"

    def test_all_recipe_records(self):
        """ Test /movies/<movieid> for all known movies"""
        for stockid, expected in GOOD_RESPONSES.items():
            expected['uri'] = "/stocks/{}".format(stockid)
            reply = requests.get("{}/{}".format(self.url, stockid))
            actual_reply = reply.json()
            self.assertEqual(set(actual_reply.items()), set(expected.items()))

    def test_not_found(self):
        invalid_id = "b18f"
        actual_reply = requests.get("{}/{}".format(self.url, invalid_id))
        self.assertEqual(actual_reply.status_code, 404,
                    "Got {} but expected 404".format(
                        actual_reply.status_code))


GOOD_RESPONSES ={
  "egg": {
    "title": "eggs",
    "quantity in stock": 6,
    "unit": "pieces",
    "id": "egg"
  },
  "milk": {
    "title": "milk",
    "quantity in stock": 200,
    "unit": "milliliters",
    "id": "milk"
  }
}

if __name__ == "__main__":
    unittest.main()
