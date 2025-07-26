# pkg-check

A simple and intuitive command-line tool to check if Python packages are installed, with smart suggestions and automatic installation capabilities.

## Features

- ✅ **Package Status Check**: Quickly verify if a Python package is installed and see its version
- 🔍 **PyPI Integration**: Automatically checks PyPI if a package isn't found locally
- 📦 **Smart Installation**: Offers to install packages directly from PyPI
- 💡 **Intelligent Suggestions**: Provides similar package name suggestions when packages aren't found
- 📋 **Dependency Information**: Shows package dependencies for installed packages
- 🌐 **Network Awareness**: Gracefully handles offline scenarios

## Installation

### From Source

1. Clone or download this repository
2. Navigate to the project directory
3. Install the package:

```bash
pip install .
```

This will install `pkg-check` as a command-line tool that you can use from anywhere.

## Usage

### Basic Usage

Check if a package is installed:

```bash
pkg-check numpy
```

### Example Outputs

**When package is installed:**
```
✅ numpy is installed (version: 1.24.3)
📦 Dependencies
- python-dateutil
- pytz
```

**When package is not installed but exists on PyPI:**
```
❌ requests is not installed
Would you like to install the package?N/y? y
✅ Installed 'requests':
Successfully installed requests-2.31.0
```

**When package doesn't exist (with suggestions):**
```
❌ numpyy is not installed
😇 Did you mean one of these packages:
 - numpy
 - numpydoc
 - numpy-stl
```

**When package doesn't exist (no suggestions):**
```
❌ nonexistentpackage123 is not installed
😓 I couldn't find it on PyPI either
```

## How It Works

1. **Local Check**: First checks if the package is installed locally using `importlib.metadata`
2. **Network Check**: If not found locally, checks internet connectivity
3. **PyPI Lookup**: Queries PyPI to see if the package exists
4. **Installation Option**: If package exists on PyPI, offers to install it
5. **Smart Suggestions**: If package doesn't exist, suggests similar package names
6. **Dependency Info**: For installed packages, shows their dependencies

## Requirements

- Python 3.7+
- `requests` library for PyPI API calls
- Internet connection (for PyPI checks and installations)

## Development

### Project Structure

```
pkg_check/
├── pkg_check.py      # Main application code
├── setup.py          # Package configuration
└── README.md         # This file
```

### Running from Source

```bash
python pkg_check.py <package_name>
```

### Building

```bash
python setup.py sdist bdist_wheel
```

## Author

**Kadilana Mbogo**  
Email: kadilanambogo@gmail.com

## License

This project is open source. Feel free to use, modify, and distribute as needed.

## Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## Changelog

### Version 0.1
- Initial release
- Basic package checking functionality
- PyPI integration
- Package installation capability
- Smart package suggestions
- Dependency information display
