import youtube_dl
from sys import argv

# Taking the YouTube video link as a command-line argument
link = argv[1]

# Options for youtube_dl
options = {
    'format': 'bestvideo+bestaudio/best',  # Get the best quality
    'outtmpl': '/Users/tauhi/Downloads/%(title)s.%(ext)s',  # Path and naming scheme for downloaded video
    'quiet': False,  # Set to True if you want to disable console messages
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Desired output format
    }],
}

with youtube_dl.YoutubeDL(options) as ydl:
    info_dict = ydl.extract_info(link, download=False)
    print("Title: ", info_dict['title'])
    print("View Count: ", info_dict['view_count'])
    ydl.download([link])
