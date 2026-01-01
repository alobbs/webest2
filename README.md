# webest2

Web automation and testing library built on Selenium.

## Installation

```bash
pip install webest2
```

## Usage

```python
import webest2

# Initialize browser
webest2.init()

# Load a URL
webest2.load("https://example.com")

# Get page title
title = webest2.get_title()
print(f"Page title: {title}")
```

## Features

- Simple browser initialization with automatic retry
- Context manager support for clean resource management
- Screenshot capabilities
- Exception handling for web automation

## Requirements

- Python 3.9+
- Selenium
- Retrying

## License

MIT
