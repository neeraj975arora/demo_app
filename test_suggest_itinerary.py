import unittest
from suggest_itinerary import suggest_itinerary

class TestSuggestItinerary(unittest.TestCase):
    def test_suggest_itinerary(self):
        result = suggest_itinerary("Paris", 3)
        self.assertEqual(result, "Plan a 3-day trip for Paris considering weather and local attractions.")
        result2 = suggest_itinerary("London", 5)
        self.assertEqual(result2, "Plan a 5-day trip for London considering weather and local attractions.")

if __name__ == "__main__":
    unittest.main() 