import yaml
from tkinter import *


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


def write(window, top_tb, extensions_lb, algorithms_lb):

    try:
        name = window.filename

    except:

        try:
            name = window.directory

        except:
            name = ''

    last_char_index = name.rfind("/")

    directory = name[:last_char_index]

    file = name[last_char_index+1:]

    try:
        top = int(top_tb.get())

    except:
        top = top_tb.get()

    list_extensions = []

    if len(extensions_lb.curselection()) > 0:

        for extension in extensions_lb.curselection():
            list_extensions.append(extensions[extension])

    dict_algorithms = {}

    if len(algorithms_lb.curselection()) > 0:

        for algorithm in algorithms_lb.curselection():
            dict_algorithms.update({algorithms[algorithm]: True})

    message = StringVar()
    message.set('')

    error = Label(window, textvariable=message, background='red')
    error.pack(fill=BOTH, expand=TRUE)

    if directory and file:
        configuration = {'directory': directory,
                         'name': file,
                         'extensions': list_extensions,
                         'algorithms': dict_algorithms,
                         'top': top}

        file = open('configuration_gui.yaml', 'w')

        yaml.dump(configuration, file)

        window.destroy()

    else:
        message.set('Path missing')

