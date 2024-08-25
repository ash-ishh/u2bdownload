# u2bdownload

u2bdownload is a simple FastHTML-based web application designed to extract video links from a given URL.

## Prerequisites

- Python 3.6+

## Installation and Setup

### Option 1: Using [uv](https://docs.astral.sh/uv/)

1. Install uv (if not already installed):
   ```
   pip install uv
   ```
   OR
   ```
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Run the application:
   ```
   uv run main.py
   ```

This will set up a virtual environment and run the application automatically.



### Option 2: Using pip

1. Create and activate a virtual environment:

   **Linux/macOS:**
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

   **Windows:**
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```
   python main.py
   ```

## TODO

- Add loader on URL submit
- Add copy link option
- Playlist link support