import os
import yt_dlp
import whisper
import shutil
import subprocess

def download_audio(url, output_path="downloads"):
    os.makedirs(output_path, exist_ok=True)
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = os.path.join(output_path, f"{info['title']}.mp3")
    return filename, output_path

def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # tiny, base, small, medium, large
    print("Transcribing audio...")
    result = model.transcribe(audio_path)
    return result["text"]

def summarise_with_llm(text):
    prompt = f"""Summarise the following into steps. 
Give only the steps and references/tips per step and nothing else.

{text}"""

    try:
        # Call Ollama CLI (make sure you installed Ollama and pulled a model, e.g., mistral)
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt.encode("utf-8"),
            capture_output=True,
            check=True
        )
        return result.stdout.decode("utf-8").strip()
    except Exception as e:
        return f"Error running LLM: {e}"

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    mp3_file, output_dir = download_audio(url)

    try:
        text = transcribe_audio(mp3_file)
        print(text)

        with open("transcription.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("\nTranscription saved to transcription.txt")

        # Summarise with free local LLM
        summary = summarise_with_llm(text)
        with open("summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)
        print("\nSummary saved to summary.txt")
        print(summary)

        # Cleanup
        if os.path.exists(mp3_file):
            os.remove(mp3_file)
            print(f"Deleted audio file: {mp3_file}")

        if os.path.isdir(output_dir) and not os.listdir(output_dir):
            os.rmdir(output_dir)
            print(f"Deleted empty directory: {output_dir}")

    except Exception as e:
        print(f"Error during transcription: {e}")
