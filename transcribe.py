#!/usr/bin/env python3

import argparse
import os
import sys

try:
    import openai
except ImportError:
    sys.exit("Please install the OpenAI library with `pip install openai`.")


def transcribe_file(input_path: str, model: str = "whisper-1") -> str:
    """
    Transcribe an audio file using OpenAI's Whisper API.

    Parameters:
    - input_path: Path to the .m4a audio file.
    - model: Whisper model to use (default: "whisper-1").

    Returns:
    - Transcribed text.
    """
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    with open(input_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe(model, audio_file)
    return transcript["text"]


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe an audio file to text using OpenAI Whisper."
    )
    parser.add_argument(
        "audio_file",
        type=str,
        help="Path to the input audio file"
    )
    parser.add_argument(
        "-m", "--model",
        type=str,
        default="whisper-1",
        help="Whisper model to use (default: whisper-1)"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Path to save the transcript text (if not provided, prints to stdout)"
    )
    args = parser.parse_args()

    # Ensure API key is set
    if not os.getenv("OPENAI_API_KEY"):
        sys.exit(
            "Error: OPENAI_API_KEY environment variable not set.\n"
            "Please set your API key: export OPENAI_API_KEY=your_key"
        )

    try:
        text = transcribe_file(args.audio_file, model=args.model)
    except Exception as e:
        sys.exit(f"Transcription failed: {e}")

    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Transcript saved to {args.output}")
        except Exception as e:
            sys.exit(f"Failed to write output file: {e}")
    else:
        print(text)


if __name__ == "__main__":
    main()
