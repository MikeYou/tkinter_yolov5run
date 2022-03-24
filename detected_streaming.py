from tkinter import *
import time
from PIL import  ImageTk, Image, ImageDraw
import cv2
import random
import os
import time
import datetime
import signal
import subprocess
import imageio
from PIL import ImageFile, Image
ImageFile.LOAD_TRUNCATED_IMAGES = True

def new_report(test_report):
    lists=os.listdir(test_report)
    lists.sort(key=lambda fn:os.path.getmtime(test_report+"//"+fn))
    return lists[-1]

def stream():
    try:
        image = video.get_next_data()
        frame_image = Image.fromarray(image)
        frame_image=ImageTk.PhotoImage(frame_image)
        l1.config(image=frame_image)
        l1.image = frame_image
        l1.after(delay, lambda: stream())
    except:
        video.close()
        return
def kill_detect():
    os.system("pkill -f /home/coco/Desktop/cocov5test/detect_servo_localweb.py")

def detect_on():
    os.system('python3 /home/coco/Desktop/cocov5test/detect_servo_localweb.py --weights /home/coco/Desktop/weights/s.engine --img 640 640 --conf 0.8 --source 0 --data /home/coco/Desktop/weights/cocoadata.yaml --agnostic-nms')
def screen():
    os.system('python3 /home/coco/Desktop/label_test3.py')


########### Main Program ############

root = Tk()
root.title("即時辨識畫面")
root.geometry("640x480")

f1=Frame(root)
l1 = Label(f1)
l1.grid(row = 1,column = 0)
f1.grid(row = 1,column = 1)

while True:
    video_name = "location of saved image"+str(new_report("location of saved image"))   #Image-path
    video = imageio.get_reader(video_name)

    stream()
    root.update()
    root.after(100)

root.mainloop()
