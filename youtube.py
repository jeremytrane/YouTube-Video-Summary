import os
import yt_dlp
import whisper

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
    return filename

def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # options: tiny, base, small, medium, large
    print("Transcribing audio")
    result = model.transcribe(audio_path)
    return result["text"]

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    mp3_file = download_audio(url)
    
    text = transcribe_audio(mp3_file)
    print(text)
    
    with open("transcription.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("\nTranscription saved to transcription.txt")
