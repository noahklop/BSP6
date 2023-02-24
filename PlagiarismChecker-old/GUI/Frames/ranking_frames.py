from tkinter import *


def get(window):
    frame1 = Frame(window)
    frame1.pack(fill=X)
    frame2 = Frame(window)
    frame2.pack(fill=X)
    frame3 = Frame(frame2)
    frame3.pack(anchor=CENTER)

    frames = [frame1, frame2, frame3]

    return frames
