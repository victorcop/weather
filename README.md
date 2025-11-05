# Weather API Module

[![CI Tests](https://github.com/victorcop/weather/actions/workflows/python-test.yml/badge.svg?branch=main)](https://github.com/victorcop/weather/actions/workflows/python-test.yml)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![GitHub](https://img.shields.io/github/stars/victorcop/weather?style=social)](https://github.com/victorcop/weather)

A simple Python script to fetch and display current weather information for any city using the wttr.in API.

## Features

- ✅ **No API key required** - Uses the free wttr.in service
- 🌍 **Global coverage** - Works for cities worldwide
- 🌡️ **Comprehensive data** - Temperature, humidity, wind speed, precipitation, and more
- 🎨 **Clean output** - Formatted display with emojis
- 📄 **MIT Licensed** - Free to use, modify, and distribute

## Requirements

- Python 3.6+
- requests library

## Installation

### Option 1: Install as a Package (Recommended)

1. **Clone the repository**:
   ```powershell
   git clone https://github.com/YOUR_USERNAME/weather.git
   cd weather
   ```

2. **Create a virtual environment** (recommended):
   ```powershell
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

4. **Install the package in editable mode**:
   ```powershell
   pip install -e .
   ```

   Or with development dependencies (includes pytest):
   ```powershell
   pip install -e ".[dev]"
   ```

### Option 2: Install Dependencies Only

```powershell
pip install -r requirements.txt
```

## Usage

### After Installing as a Package

If you installed with `pip install -e .`, you can run the weather command from anywhere:

```powershell
weather
```

Or run as a Python module:

```powershell
python -m weather
```

### Without Installing

Navigate to the project directory and run:

```powershell
python -m weather
```

You'll be prompted to enter a city name. Press Enter without typing anything to use the default (London).

### Example Output

```
Enter city name (or press Enter for London): Sabaneta

🌤️  Weather for Sabaneta, Colombia
==================================================
Temperature: 14°C / 57°F
Feels Like: 14°C / 57°F
Condition: Light rain shower
Humidity: 97%
Wind: 4 km/h NE
Precipitation: 0.6 mm
Cloud Cover: 61%
```

## Project Structure

```
weather/
├── src/
│   └── weather/          # Main package
│       ├── __init__.py
│       ├── __main__.py   # CLI entry point
│       └── weather.py    # Core weather functionality
├── tests/                # Test suite
│   ├── __init__.py
│   └── test_weather.py
├── .github/
│   └── workflows/        # CI/CD pipelines
│       └── python-test.yml
├── pyproject.toml        # Package configuration
├── requirements.txt      # Runtime dependencies
├── README.md
├── LICENSE
├── CONTRIBUTING.md
└── .gitignore
```

## How It Works

The script uses the [wttr.in](https://wttr.in) API, which provides weather data in JSON format without requiring authentication. The API endpoint format is:

```text
https://wttr.in/{city}?format=j1
```

The script:

1. Takes a city name as input
2. Makes an HTTP GET request to the wttr.in API
3. Parses the JSON response
4. Displays formatted weather information

## API Information

**API Used**: wttr.in  
**Authentication**: None required  
**Rate Limits**: Reasonable usage (no official limit published)  
**Documentation**: <https://github.com/chubin/wttr.in>

## Testing

Run the test suite to verify everything works:

```powershell
pytest
```

Or with verbose output:

```powershell
pytest -v
```

The tests verify:

- ✅ Successful weather data retrieval
- ✅ Error handling for API failures
- ✅ Default city behavior (London)

## Troubleshooting

### ModuleNotFoundError: No module named 'requests'

Make sure you've installed the requirements:
```powershell
pip install -r requirements.txt
```

### Virtual environment not activating

If you get an execution policy error on Windows:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Wrong Python version

Ensure you're using the correct Python installation. You can specify the full path:
```powershell
C:/Users/YourUsername/AppData/Local/Microsoft/WindowsApps/python3.13.exe weather.py
```

## Contributing

Contributions are welcome! We use a **Git Flow** branching strategy:

- **`main`** - Production-ready code
- **`dev`** - Integration branch (target for PRs)
- **`feature/*`** - New features

**Quick start:**
1. Fork the repo
2. Create a feature branch from `dev`: `git checkout -b feature/my-feature`
3. Make your changes and add tests
4. Open a PR to `dev` branch

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

This software is free to use, modify, and distribute. You can:

- ✅ Use it commercially
- ✅ Modify and distribute it
- ✅ Use it privately
- ✅ Include it in other projects

The only requirement is to include the original copyright notice and license text in any substantial portions of the software.
