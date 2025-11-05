"""
Main entry point for the weather module.
"""
from .weather import get_weather


def main():
    """Main function to run the weather CLI."""
    # Get user input
    city = input("Enter city name (or press Enter for London): ").strip()
    if not city:
        city = "London"
    
    get_weather(city)


if __name__ == "__main__":
    main()
