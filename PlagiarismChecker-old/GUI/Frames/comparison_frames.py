from tkinter import *


def get(top):
    frame1 = Frame(top)
    frame1.pack(fill=X)
    frame2 = Frame(top)
    frame2.pack(fill=X)
    frame3 = Frame(frame1)
    frame3.pack(fill=BOTH, side=LEFT, expand=TRUE)
    frame4 = Frame(frame1)
    frame4.pack(fill=BOTH, side=RIGHT, expand=TRUE)
    frame5 = Frame(frame2)
    frame5.pack(anchor=CENTER)

    frames = [frame1, frame2, frame3, frame4, frame5]

    return frames
