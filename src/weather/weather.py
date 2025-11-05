import requests

def get_weather(city="London"):
    """
    Get weather information using wttr.in API (no authentication required)
    
    Args:
        city: City name (default: London)
    """
    # wttr.in API endpoint - returns JSON format
    url = f"https://wttr.in/{city}?format=j1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract current weather
        current = data['current_condition'][0]
        location = data['nearest_area'][0]
        
        print(f"\n🌤️  Weather for {location['areaName'][0]['value']}, {location['country'][0]['value']}")
        print(f"{'='*50}")
        print(f"Temperature: {current['temp_C']}°C / {current['temp_F']}°F")
        print(f"Feels Like: {current['FeelsLikeC']}°C / {current['FeelsLikeF']}°F")
        print(f"Condition: {current['weatherDesc'][0]['value']}")
        print(f"Humidity: {current['humidity']}%")
        print(f"Wind: {current['windspeedKmph']} km/h {current['winddir16Point']}")
        print(f"Precipitation: {current['precipMM']} mm")
        print(f"Cloud Cover: {current['cloudcover']}%")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError as e:
        print(f"Error parsing weather data: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Get user input
    city = input("Enter city name (or press Enter for London): ").strip()
    if not city:
        city = "London"
    
    get_weather(city)
