from tkinter import filedialog
from tkinter import *
from functools import partial
from GUI import write_configuration_gui
from GUI.Frames import configuration_frames
import os


def file_button_clicked(window, frame):
    window.filename = filedialog.askopenfilename(initialdir=os.environ["HOME"],
                                                 title="Select file",
                                                 filetypes=(("zip files", "*.zip"),))
    Label(frame, text=window.filename).pack(side=RIGHT)


def directory_button_clicked(window, frame):
    window.directory = filedialog.askdirectory(initialdir=os.environ["HOME"],
                                               title="Select directory")
    Label(frame, text=window.directory).pack(side=RIGHT)


def more_less_clicked(more_less, frames):
    if more_less.get() == 'Show more':
        more_less.set('Show less')

        for i in range(11, 15):
            frames[i].pack(fill=X)

    elif more_less.get() == 'Show less':
        more_less.set('Show more')

        for i in range(11, 15):
            frames[i].pack_forget()


extensions = ['swift',
              'java',
              'py',
              'cs',
              'c']

algorithms = ['Cosine similarity',
              'Bag distance',
              'Jaccard index',
              'Sørensen–Dice coefficient',
              'Tversky index',
              'Overlap coefficient',
              'Tanimoto distance']


def run(window):
    frames = configuration_frames.get(window)
    more_less = StringVar()
    more_less.set('Show more')

    for i in range(11, 15):
        frames[i].pack_forget()

    Label(frames[1], text='FILE OR DIRECTORY\nSelect file or directory that contains the assignments to be compared', background='lightgrey', justify=LEFT).pack(pady=5, side=LEFT)
    Button(frames[2], text='File', command=partial(file_button_clicked, window, frames[2])).pack(padx=5, pady=15, side=LEFT)
    Label(frames[2], text='OR').pack(pady=15, side=LEFT)
    Button(frames[2], text='Directory', command=partial(directory_button_clicked, window, frames[2])).pack(padx=5, pady=15, side=LEFT)

    Label(frames[11], text='ALGORITHMS\nAlgorithms used to compare the files', background='lightgrey', justify=LEFT).pack(pady=5, side=LEFT)
    Label(frames[13], text='EXTENSIONS\nExtensions of the files to be compared', background='lightgrey', justify=LEFT).pack(pady=5, side=LEFT)

    algorithms_lb = Listbox(frames[12], selectmode=MULTIPLE, exportselection=0, borderwidth=0)
    algorithms_lb.pack(side=LEFT, fill=X, expand=TRUE, padx=10, pady=5)
    for item in algorithms:
        algorithms_lb.insert(END, item)

    extensions_lb = Listbox(frames[14], selectmode=MULTIPLE, exportselection=0, borderwidth=0)
    extensions_lb.pack(side=LEFT, fill=X, expand=TRUE, padx=10, pady=5)
    for item in extensions:
        extensions_lb.insert(END, item)

    Label(frames[6], text='TOP\nNumber of plagiarisms to show', background='lightgrey', justify=LEFT).pack(pady=5, side=LEFT)
    Label(frames[8], text='CONFIGURATION\nSkip to use YAML configuration', background='lightgrey', justify=LEFT).pack(pady=5, side=LEFT)

    top_tb = Entry(frames[7])
    top_tb.pack(side=LEFT, fill=X, expand=TRUE, padx=10, pady=7)

    Button(frames[10], text='Run', command=partial(write_configuration_gui.write, window, top_tb, extensions_lb, algorithms_lb)).pack(padx=5, pady=10, side=LEFT)
    Button(frames[10], textvariable=more_less, command=partial(more_less_clicked, more_less, frames)).pack(padx=5, pady=10, side=LEFT)
