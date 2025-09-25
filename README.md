# YouTube Video Summary

A Python tool that downloads YouTube videos, transcribes the audio using OpenAI Whisper, and generates AI-powered summaries using local Ollama models.

## Features

- Downloads audio from YouTube videos using yt-dlp
- Transcribes audio to text using OpenAI Whisper
- Generates step-by-step summaries using local Ollama LLM (Mistral)
- Automatic cleanup of temporary audio files
- Virtual environment management

## Prerequisites

### System Requirements
- **Python 3.7+**
- **FFmpeg** - Required for audio processing
- **Ollama** - For local LLM inference

### Installing Prerequisites

#### Windows
1. **Python**: Download from [python.org](https://www.python.org/downloads/)
2. **FFmpeg**:
   - Download from [ffmpeg.org](https://ffmpeg.org/download.html)
   - Add to PATH or place in project directory
3. **Ollama**:
   - Download from [ollama.com](https://ollama.com/)
   - After installation, pull the Mistral model: `ollama pull mistral`

#### macOS
```bash
# Install using Homebrew
brew install python ffmpeg
brew install ollama

# Pull the Mistral model
ollama pull mistral
```

#### Linux (Ubuntu/Debian)
```bash
# Install system dependencies
sudo apt update
sudo apt install python3 python3-pip python3-venv ffmpeg

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull the Mistral model
ollama pull mistral
```

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jeremytrane/YouTube-Video-Summary.git
   cd YouTube-Video-Summary
   ```

2. **Set up virtual environment and install dependencies:**

   **Option A: Using the setup script (Linux/macOS)**
   ```bash
   chmod +x start.sh
   ./start.sh
   ```

   **Option B: Manual setup (all platforms)**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate

   # Upgrade pip and install dependencies
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Verify Ollama is running:**
   ```bash
   # Start Ollama service (if not already running)
   ollama serve

   # Test the model (in another terminal)
   ollama run mistral "Hello, world!"
   ```

## Usage

### Interactive Mode
```bash
python youtube.py
# Enter YouTube URL when prompted
```

### Command Line Mode
```bash
python youtube.py
# Then paste your YouTube URL when prompted
```

### Example
```bash
python youtube.py
# Enter YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

The tool will:
1. Download audio from the YouTube video
2. Transcribe the audio to text (saved as `transcription.txt`)
3. Generate a summary using Ollama Mistral (saved as `summary.txt`)
4. Clean up temporary audio files

## Configuration

### Whisper Model Options
Edit `youtube.py` line 27 to change the Whisper model:
```python
model = whisper.load_model("base")  # Options: tiny, base, small, medium, large
```

- `tiny` - Fastest, least accurate (~39 MB)
- `base` - Good balance (~142 MB)
- `small` - Better accuracy (~488 MB)
- `medium` - High accuracy (~1.5 GB)
- `large` - Best accuracy (~2.9 GB)

### Ollama Model Options
Edit `youtube.py` line 41 to use different models:
```python
result = subprocess.run(["ollama", "run", "mistral"], ...)
```

Available models (run `ollama list` to see installed):
- `mistral` - Default, good performance
- `llama3.2` - Alternative option
- `codellama` - For code-focused content

## Project Structure

```
YouTube-Video-Summary/
├── youtube.py          # Main application script
├── start.sh           # Setup script for Unix systems
├── requirements.txt   # Python dependencies
├── README.md         # This file
├── .gitignore        # Git ignore rules
├── venv/             # Virtual environment (created after setup)
├── transcription.txt # Generated transcription (gitignored)
└── summary.txt       # Generated summary (gitignored)
```

## Dependencies

- **yt-dlp** - YouTube video/audio downloader
- **pydub** - Audio processing library
- **openai-whisper** - Speech-to-text transcription
- **torch** - PyTorch for Whisper model inference

## Troubleshooting

### Common Issues

**FFmpeg not found:**
```
Error: ffmpeg not found
```
- Ensure FFmpeg is installed and in your PATH
- On Windows, download from ffmpeg.org and add to PATH

**Ollama connection error:**
```
Error running LLM: [Errno 2] No such file or directory: 'ollama'
```
- Install Ollama from ollama.com
- Start Ollama service: `ollama serve`
- Pull required model: `ollama pull mistral`

**CUDA/GPU issues with Whisper:**
- Whisper will automatically use CPU if CUDA is unavailable
- For GPU acceleration, ensure PyTorch is installed with CUDA support

**Permission denied on start.sh:**
```bash
chmod +x start.sh
```

### Performance Tips

- Use smaller Whisper models (`tiny`, `base`) for faster processing
- Ensure sufficient RAM for larger models
- GPU acceleration significantly speeds up Whisper transcription

## License

MIT License - Feel free to use and modify for your projects.
