import os
import cv2
from pytube import YouTube
from youtubesearchpython import VideosSearch
from tqdm import tqdm
import yt_dlp
from googleapiclient.discovery import build

API_KEY = "AIzaSyDSOp-zDUGNictntDW8OyLvp-fqvujbWrU"
YOUTUBE = build("youtube", "v3", developerKey=API_KEY)
urls = ["https://www.youtube.com/shorts/B_CxVGNzefk", "https://www.youtube.com/shorts/FjeouIqEu20", "https://www.youtube.com/watch?v=ejx06woQGA0" ]

video_counter =0

os.makedirs('downloads', exist_ok=True)

os.makedirs('frames', exist_ok=True)


for i in urls:

    output_template = f"downloads/video{video_counter}.%(ext)s"

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': output_template,
        'quiet': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(i)

    print(f"Video {video_counter} downloaded successfully!")


    capture = cv2.VideoCapture(f'./downloads/video{video_counter}.mp4')

    os.makedirs(f'frames/video{video_counter}', exist_ok=True)

    frame_counter = 0
    while (capture.isOpened()):
        ret, frame = capture.read()
        if ret== False:
            break

        cv2.imwrite(f'./frames/video{video_counter}/frame' +  str(frame_counter) + ".png", frame)
        frame_counter +=1

    capture.release()
    video_counter +=1
    print(f"{frame_counter} video captured succesfully")





