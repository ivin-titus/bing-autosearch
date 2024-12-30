# Bing Search Automation

Automate Bing searches using Python and GUI automation. Lightweight script that simulates keyboard & mouse inputs using pyautogui.

## Features

- Automated Bing searches
- Scheduled search execution
- Windows & Linux support
- GUI-based automation (low detection risk)
- Configurable search parameters

## Prerequisites

- Computer with GUI (minimum 540p resolution)
- Internet connection (4+ Mbps)
- Google Chrome (latest version)
- Python 3.10+

## Dependencies

```bash
pip install pyautogui pygetwindow requests
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/[username]/bing-search-automation
cd bing-search-automation
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Execution
```bash
python run.py
```

### Scheduled Execution
```bash
python run-at.py
```

## Important Notes

- Do not interact with keyboard/mouse during script execution
- Script requires proper Bing account login for Rewards functionality
- Only performs PC searches (mobile searches not supported)
- Compatible with Windows/Linux (MacOS untested, mobile OS unsupported)
- Uses GUI automation instead of web scripting for reduced detection risk

## Version Compatibility

⚠️ **Notice**: Versions below v2.0 are no longer functional due to Bing Rewards program changes.

## Customization

Refer to `readme.txt` in each version directory for customization options and version-specific features.

## Limitations

- Account suspension risk exists (though minimized through GUI automation)
- Mobile searches not supported
- No automatic completion of other Bing Rewards tasks

## Support

- Report issues via GitHub Issues
- Contact via ivintitus@hotmail.com 


## License


---
Created by Ivin Titus
