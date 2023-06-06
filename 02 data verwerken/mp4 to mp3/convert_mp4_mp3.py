from moviepy.editor import VideoFileClip

# Specify the path to the input MP4 video file
input_file = "C:\\Users\\timH\\OneDrive - Ortec B.V\\private\\trouw\\muziek\\dj\\07 openingsdans summer jam\\summer_jam.mp4"

# Specify the path to save the output MP3 audio file
output_file = "output_audio.mp3"

# Load the video clip
video_clip = VideoFileClip(input_file)

# Extract the audio from the video clip
audio_clip = video_clip.audio

# Save the audio clip as an MP3 file
audio_clip.write_audiofile(output_file, codec="mp3")

# Close the clips
video_clip.close()
audio_clip.close()
