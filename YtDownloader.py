import yt_dlp
import sys

# 1. Define the "How-To" (The Function)
def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Fetching info...")
            ydl.download([url])
        print("\nDownload complete!")
    except Exception as e:
        print(f"An error occurred: {e}")

# 2. Define the "When-To-Run" (The Entry Point)
if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        download_video(video_url)
    else:
        print("Usage: python YtDownloader.py [URL]")