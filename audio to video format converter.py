import moviepy.editor

from pathlib import Path

video_file = Path('video.mp4')

video = moviepy.editor.VideoClip(f'{video_file}')
# video = moviepy.editor.VideoClip('video.mp4')
audio = video.audio

# audio.write_audiofile('audio.mp3')
audio.write_audiofile(f'{video_file.stem}.mp3')
