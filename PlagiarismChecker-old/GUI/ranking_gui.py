from tkinter import *
from functools import partial
from GUI import results_gui, comparison_gui
from GUI.Frames import ranking_frames


def run(window, results, run_time, config):
    frames = ranking_frames.get(window)
    top = config.top

    for key1, value1 in results.ranking.items():
        path1 = value1[0].path
        path2 = value1[1].path

        result = path1.replace(config.get_directory().path, '') + '\n'
        result += path2.replace(config.get_directory().path, '')

        Button(frames[0], text=result, command=partial(comparison_gui.show, window, value1, config)).pack(padx=10, pady=5)

    Button(frames[2], text='Results', command=partial(results_gui.show, window, results, run_time, config)).pack(padx=5, pady=5, side=LEFT)
    Button(frames[2], text='Help', command=partial(show_help, window, top)).pack(padx=5, pady=5, side=LEFT)
    Button(frames[2], text='Quit', command=window.destroy).pack(padx=5, pady=5, side=LEFT)


def show_help(window, top):
    help_top = Toplevel(window)
    help_top.title('HELP')

    help_text = 'List of top ' + str(top) + ' pair of files most likely to be ' + '\n' + \
                'plagiarized. Ordered from most likely to be plagiarism at the ' + '\n' + \
                'top, to less likely to be plagiarism at the bottom.'

    Label(help_top, text=help_text).pack(pady=5)
    Button(help_top, text='Quit', command=help_top.destroy).pack(pady=5)

    help_top.mainloop()

