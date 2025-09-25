# YouTube-Video-Summary

A small tool that fetches a YouTube video and generates a summary.

## Requirements

- Python 3.x  
- Dependencies listed in `requirements.txt`

## Installation & Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/jeremytrane/YouTube-Video-Summary.git
   cd YouTube-Video-Summary
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Make `start.sh` executable (if on Unix-like OS):  
   ```bash
   chmod +x start.sh
   ```

## Usage

- Run via shell script:  
  ```bash
  ./start.sh <YouTube-URL>
  ```

- Or run directly with Python:  
  ```bash
  python youtube.py <YouTube-URL>
  ```

The script will fetch the video and output a summary.

## Files

- `youtube.py` — main script  
- `start.sh` — wrapper script to launch with a URL  
- `requirements.txt` — Python dependencies  

## License

Specify your license here (e.g. MIT, Apache, etc.).
