import unittest
from unittest.mock import patch
from get_weather import get_weather

class TestGetWeather(unittest.TestCase):
    @patch('get_weather.requests.get')
    @patch('get_weather.os.getenv', return_value='dummy_api_key')
    def test_get_weather_success(self, mock_getenv, mock_get):
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "weather": [{"description": "clear sky"}],
            "main": {"temp": 22.5}
        }
        result = get_weather("London")
        self.assertIn("Weather in London: Clear sky, 22.5°C", result)

    @patch('get_weather.requests.get')
    @patch('get_weather.os.getenv', return_value='dummy_api_key')
    def test_get_weather_api_error(self, mock_getenv, mock_get):
        mock_response = mock_get.return_value
        mock_response.raise_for_status.side_effect = Exception("API error")
        result = get_weather("London")
        self.assertIn("Could not fetch weather for London", result)

    @patch('get_weather.os.getenv', return_value=None)
    def test_get_weather_no_api_key(self, mock_getenv):
        result = get_weather("London")
        self.assertIn("OpenWeatherMap API key not found", result)

if __name__ == "__main__":
    unittest.main() 