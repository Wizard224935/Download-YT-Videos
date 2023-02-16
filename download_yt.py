from pytube import YouTube

# prompt user to enter video url
url = input("https://www.youtube.com/watch?v=pGu2MiVZ3bY&list=LL&index=27")

# create YouTube object and get the first stream
yt = YouTube(url)
stream = yt.streams.first()

# download the video
print(f"Downloading {yt.title}...")
stream.download()
print("Download completed!")
