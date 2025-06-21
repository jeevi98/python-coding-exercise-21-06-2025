from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        print(f"\n Title: {yt.title}")
        print(f" Channel: {yt.author}")
        print(f" Published on: {yt.publish_date}")
        print(f" Length: {yt.length // 60} min {yt.length % 60} sec")
        print(f" Views: {yt.views:,}")

        stream = yt.streams.get_highest_resolution()

        print("\n⬇ Downloading...")
        stream.download()
        print(" Download complete!")
    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    download_video(video_url)
