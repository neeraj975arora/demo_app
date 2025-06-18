import unittest
from tools import search_places_tool, get_weather_tool, find_hotels_tool
from suggest_itinerary import suggest_itinerary

class TestTools(unittest.TestCase):
    def test_search_places_tool(self):
        result = search_places_tool.run("Paris")
        self.assertIn("Points of interest in Paris", result)

    def test_get_weather_tool(self):
        # Simulate with a city that will likely fail gracefully (no API key in test)
        result = get_weather_tool.run("Paris")
        self.assertTrue("Weather in Paris" in result or "Could not fetch weather for Paris" in result or "API key" in result)

    def test_find_hotels_tool(self):
        result = find_hotels_tool.run("Paris")
        self.assertIn("Hotel options in Paris", result)

    def test_suggest_itinerary_tool(self):
        self.assertIn("Plan a 3-day trip for Paris", suggest_itinerary("Paris", 3))

if __name__ == "__main__":
    unittest.main() 