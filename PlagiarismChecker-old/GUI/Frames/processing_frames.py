from tkinter import *


def get(window):
    frame1 = Frame(window)
    frame1.pack(fill=X)
    frame2 = Frame(frame1)
    frame2.pack(fill=X, expand=TRUE, anchor=CENTER)

    frames = [frame1, frame2]

    return frames
