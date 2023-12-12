import glob

from moviepy.editor import *
import os
if os.name=='nt':
    os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"
elif os.name=='posix':
    os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/Cellar/ffmpeg/5.1/bin/ffmpeg"


files = glob.glob("./srcmovie/*")
videoclips=[]
audioclips=[]
for file in files:
    videoclips.append(VideoFileClip(file).resize(width=480))
    audioclips.append(AudioFileClip(file))

save_path = "newmovie/movie.mp4"#保存先のpath

#動画の連結
final_clip = concatenate_videoclips(videoclips)
final_clip.audio= concatenate_audioclips(audioclips)
final_clip.write_videofile(save_path, fps=24, audio=True, codec='libx264',audio_codec='aac', temp_audiofile='temp-audio.m4a',remove_temp=True) #動画の書き込み
# final_clip.write_videofile("output.mp4", codec="libx264", audio_codec="aac")
