import glob

from moviepy.editor import *


files = glob.glob("./srcmovie/*")
videoclips=[]
audioclips=[]
for file in files:
    videoclips.append(VideoFileClip(file).resize(0.4))
    audioclips.append(AudioFileClip(file))

save_path = "newmovie/movie.mp4"#保存先のpath

#動画の連結
final_clip = concatenate_videoclips(videoclips)
final_clip.audio= concatenate_audioclips(audioclips)
final_clip.write_videofile(save_path, fps=24, audio=True, codec='libx264',audio_codec='aac', temp_audiofile='temp-audio.m4a',remove_temp=True) #動画の書き込み