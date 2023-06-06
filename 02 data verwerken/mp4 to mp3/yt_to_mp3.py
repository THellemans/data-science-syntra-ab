import subprocess

def convert_to_mp3(youtube_link):
    try:
        # Run youtube-dl to extract audio
        command = f"youtube-dl -x --audio-format mp3 --audio-quality 0 {youtube_link}"
        subprocess.call(command, shell=True)

        print("Conversion completed successfully.")
    except Exception as e:
        print("An error occurred during conversion:", str(e))

# Example usage

youtube_links = ['https://www.youtube.com/watch?v=MK6TXMsvgQg',
					'https://www.youtube.com/watch?v=c7O91GDWGPU',
					'https://www.youtube.com/watch?v=XAYhNHhxN0A',
					'https://www.youtube.com/watch?v=Nx5c_JZIM6M',
					'https://www.youtube.com/watch?v=aYAJopwEYv8']

for youtube_link in youtube_links:
	song = convert_to_mp3(youtube_link)
	print(song)
	print('success')
