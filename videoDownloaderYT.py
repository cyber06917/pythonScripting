# Install ffmpeg and yt-dlp on your platform of choice.  
# yt-dlp uses ffmpeg to download videos above 720p, as YouTube streams video and audio separately at higher qualities.  
# ffmpeg is used here to merge the video and audio streams.  
# This script downloads the video in the best available quality and saves it to the specified directory.  
# It displays the download progress and the final saved location.  


import yt_dlp

def download_youtube_video(url, save_path="."):
    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4][height<=2160]+bestaudio[ext=m4a]/bestvideo[ext=mp4][height<=1440]+bestaudio[ext=m4a]/bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]',  # Download the best quality video + audio
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save with video title in the specified directory
            'progress_hooks': [download_hook],  # Show progress updates
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video information
            info_dict = ydl.extract_info(url, download=False)
            print(f"Title: {info_dict.get('title', 'N/A')}")

            print("Downloading...")
            ydl.download([url])
            print(f"Download completed! Saved to: {save_path}")

    except Exception as e:
        print(f"Error: {e}")

def download_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '').strip()
        speed = d.get('_speed_str', 'N/A').strip()
        eta = d.get('_eta_str', 'N/A').strip()
        print(f"Downloading... {percent} | Speed: {speed} | ETA: {eta}", end='\r')
    elif d['status'] == 'finished':
        print("\nDownload finished, finalizing...")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_folder = input("Enter the folder path to save the video (leave blank for current directory): ") or "."
    download_youtube_video(video_url, download_folder)