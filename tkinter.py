from threading import Thread
import tkinter
import os
import subprocess

window = tkinter.Tk()
window.title("可可豆AI辨識")
def fun1():
     os.system('python3 [location of detect.py] --weights [location of weights] --img 640 --conf 0.85  --source 0 --data [location of cocoadata.yaml]')
def fun2():
     os.system('python3 [detected_streaming.py]')


def clicked1():
     Thread(target = fun1).start()

def clicked2():
     Thread(target = fun2).start()


bt = tkinter.Button(window,text="啟動辨識",command=clicked1, font=('Helvetica','80')).pack()
bt = tkinter.Button(window,text="即時辨識畫面",command=clicked2, font=('Helvetica','80')).pack()


window.geometry('400x200')
window.mainloop()
