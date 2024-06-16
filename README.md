# Hello World Chrome Extension

This is a simple Chrome extension that stores a value using the `chrome.storage` API and a Python script to fetch that value from the local LevelDB database.

## Chrome Extension

- `manifest.json`: Defines the extension's metadata and permissions.
- `background.js`: Sets the `hello` value.
- `popup.html`: Displays the stored `hello` value.

### Loading the Extension

1. Open Chrome and go to `chrome://extensions/`.
2. Enable "Developer mode".
3. Click "Load unpacked" and select the `my_extension` directory.

## Python Script

- `fetch_value.py`: Fetches the stored `hello` value from the LevelDB database.

### Requirements

- Python 3.x
- `plyvel` library (install using `pip install plyvel`)

### Usage

1. Find your extension ID in Chrome.
2. Replace `YOUR_EXTENSION_ID` in `fetch_value.py` with your extension's ID.
3. Run the script:
   ```bash
   python fetch_value.py
