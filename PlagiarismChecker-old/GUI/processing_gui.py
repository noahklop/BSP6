import time
from tkinter import *
from GUI.Frames import processing_frames


def run(window, phase, start):
    frames = processing_frames.get(window)

    end = time.time()
    run_time = str(round(end - start, 2)) + ' secs.'

    Label(frames[1], text=phase).pack(padx=5, pady=5, side=LEFT)
    Label(frames[1], text=run_time).pack(padx=5, pady=5, side=RIGHT)

    window.update()

    return run_time
