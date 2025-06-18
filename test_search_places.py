import unittest
from unittest.mock import patch
from search_places import search_places

class TestSearchPlaces(unittest.TestCase):
    @patch('search_places.requests.get')
    def test_search_places_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = [
            {"display_name": "Eiffel Tower, Paris, France", "type": "tourism"},
            {"display_name": "Louvre Museum, Paris, France", "type": "museum"}
        ]
        result = search_places("Paris")
        self.assertIn("Eiffel Tower", result)
        self.assertIn("Louvre Museum", result)
        self.assertIn("Points of interest in Paris", result)

    @patch('search_places.requests.get')
    def test_search_places_no_results(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = []
        result = search_places("NowhereCity")
        self.assertEqual(result, "No places found for NowhereCity.")

if __name__ == "__main__":
    unittest.main() 