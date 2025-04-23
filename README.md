# Transcribe CLI

Simple CLI tool to transcribe audio files using OpenAI's Whisper model.

## Quick Start


1. Set up a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate       # on macOS/Linux
# OR
.\.venv\Scripts\Activate.ps1    # on Windows (PowerShell)
```

2. Install the required packages:

```
pip install -r requirements.txt
```

3. Make it executable:

```
chmod +x transcribe.py
```

4. Profit

```
OPEN_API_KEY=YOUR_SECRET_KEY ./transcribe.py path/to/audio.m4a -o transcript.txt
```
