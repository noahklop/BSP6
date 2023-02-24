from tkinter import *


def get(top):
    frame1 = Frame(top)
    frame1.pack(fill=X, expand=TRUE)
    frame2 = Frame(top)
    frame2.pack(fill=X)
    frame3 = Frame(frame2)
    frame3.pack(anchor=CENTER)

    frames = [frame1, frame2, frame3]

    return frames
