import youtube_dl
import requests
import os
from urllib.parse import urlparse
import time

def get_ytstreams(video_url):
    ydl = youtube_dl.YoutubeDL()
    video_url = 'https://www.youtube.com/watch?v=k4rLJD7E0D0'
    info_dict = ydl.extract_info(video_url, download=False)
    url={}
    if 'formats' in info_dict:
        print("Available streams:")
        for stream in info_dict['formats']:
            print(stream['format_id'],stream['format'],stream['ext'], stream['acodec'], stream['vcodec'], stream['format_note'])
            url[stream['format_id']]=stream['url']
    format_id = input("Enter the format ID of the desired stream: ")

    ydl_opts = {
        'format': format_id,
    }
    if 'formats' in info_dict:
        return info_dict['formats']
    return None

def format_size(size):
    # Helper function to convert bytes to a human-readable format
    power = 2 ** 10
    n = 0
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    while size >= power and n < len(units) - 1:
        size /= power
        n += 1
    return f"{size:.2f} {units[n]}"


def download_file(url, destination=None):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    if not destination:
        parsed_url = urlparse(url)
        file_name = os.path.basename(parsed_url.path)
        destination = file_name if file_name else 'downloaded_file'

    file_size = int(response.headers.get('Content-Length', 0))
    downloaded_size = 0
    start_time = time.time()

    with open(destination, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
                downloaded_size += len(chunk)
                elapsed_time = time.time() - start_time
                download_speed = downloaded_size / elapsed_time
                download_percentage = (downloaded_size / file_size) * 100

                progress = f"Downloaded: {format_size(downloaded_size)}/{format_size(file_size)} " \
                           f"({download_percentage:.2f}%), Speed: {format_size(download_speed)}/s"
                print(progress, end='\r')

    print()  # Print a newline after the download completes
    return destination
# Example usage

