from tkinter import *


def title(frame):
    fr = Frame(frame, background='lightgrey')
    fr.pack(fill=X)
    return fr


def content(frame):
    fr = Frame(frame)
    fr.pack(fill=X)
    return fr


def get(window):
    frame1 = Frame(window)
    frame1.pack(fill=X)
    frame2 = title(frame1)
    frame3 = content(frame1)
    frame4 = Frame(window)
    frame4.pack(fill=BOTH)
    frame5 = Frame(frame4, borderwidth=1, relief='solid')
    frame5.pack(fill=BOTH, side=LEFT, expand=TRUE)
    frame6 = Frame(frame4, borderwidth=1, relief='solid')
    frame6.pack(fill=BOTH, side=RIGHT, expand=TRUE)
    frame7 = title(frame5)
    frame8 = content(frame5)
    frame9 = title(frame6)
    frame10 = content(frame6)
    frame11 = Frame(frame10)
    frame11.pack(anchor=CENTER)
    frame12 = title(frame5)
    frame13 = content(frame5)
    frame14 = title(frame6)
    frame15 = content(frame6)

    frames = [frame1, frame2, frame3, frame4, frame5, frame6, frame7,
              frame8, frame9, frame10, frame11, frame12, frame13, frame14,
              frame15]

    return frames
