from pytube import YouTube

# URL of the YouTube video we want to download
video_url = 'https://youtu.be/oZEmnsKLvJo?si=1DaoSjIrLqqHlWz0'

# Create a YouTube object to interact with the video
yt = YouTube(video_url)

# Get the video stream with the highest resolution available
highest_resolution_stream = yt.streams.get_highest_resolution()

# Download the video stream to the specified path
highest_resolution_stream.download('path/to/save/video.mp4')  # Assuming .mp4 format

print("Download of the highest resolution video completed!")
