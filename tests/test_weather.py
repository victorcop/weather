"""
Simple tests for the weather module
"""
import pytest
from unittest.mock import patch, MagicMock
from weather.weather import get_weather


def test_get_weather_success(capsys):
    """Test successful weather retrieval"""
    # Mock response data
    mock_response = MagicMock()
    mock_response.json.return_value = {
        'current_condition': [{
            'temp_C': '20',
            'temp_F': '68',
            'FeelsLikeC': '19',
            'FeelsLikeF': '66',
            'weatherDesc': [{'value': 'Sunny'}],
            'humidity': '65',
            'windspeedKmph': '15',
            'winddir16Point': 'NW',
            'precipMM': '0.0',
            'cloudcover': '10'
        }],
        'nearest_area': [{
            'areaName': [{'value': 'London'}],
            'country': [{'value': 'United Kingdom'}]
        }]
    }
    mock_response.raise_for_status = MagicMock()
    
    with patch('weather.weather.requests.get', return_value=mock_response):
        get_weather("London")
        captured = capsys.readouterr()
        assert "London" in captured.out
        assert "20°C" in captured.out


def test_get_weather_api_error(capsys):
    """Test handling of API errors"""
    with patch('weather.weather.requests.get', side_effect=Exception("API Error")):
        get_weather("InvalidCity")
        captured = capsys.readouterr()
        assert "Error" in captured.out or "error" in captured.out.lower()


def test_get_weather_default_city(capsys):
    """Test that default city is London"""
    mock_response = MagicMock()
    mock_response.json.return_value = {
        'current_condition': [{
            'temp_C': '15',
            'temp_F': '59',
            'FeelsLikeC': '14',
            'FeelsLikeF': '57',
            'weatherDesc': [{'value': 'Cloudy'}],
            'humidity': '70',
            'windspeedKmph': '10',
            'winddir16Point': 'N',
            'precipMM': '0.0',
            'cloudcover': '50'
        }],
        'nearest_area': [{
            'areaName': [{'value': 'London'}],
            'country': [{'value': 'United Kingdom'}]
        }]
    }
    mock_response.raise_for_status = MagicMock()
    
    with patch('weather.weather.requests.get', return_value=mock_response) as mock_get:
        get_weather()  # No city specified
        mock_get.assert_called_once()
        assert "London" in mock_get.call_args[0][0]
