import unittest
from find_hotels import find_hotels

class TestFindHotels(unittest.TestCase):
    def test_find_hotels_known_city(self):
        result = find_hotels("Paris")
        self.assertIn("Hotel Le Meurice", result)
        self.assertIn("Hotel Lutetia", result)
        self.assertIn("Hotel Regina Louvre", result)
        self.assertIn("Hotel options in Paris", result)

    def test_find_hotels_unknown_city(self):
        city = "Springfield"
        result = find_hotels(city)
        self.assertIn(f"{city} Grand Hotel", result)
        self.assertIn(f"{city} Central Inn", result)
        self.assertIn(f"{city} Suites", result)
        self.assertIn(f"Hotel options in {city}", result)

if __name__ == "__main__":
    unittest.main() 