from tkinter import *
from functools import partial
from collections import defaultdict
from GUI.Frames import result_frames

configuration = {}


def show(window, results, run_time, config):
    global configuration
    configuration = config

    results_top = Toplevel(window)
    results_top.title('RESULTS')

    frames = result_frames.get(results_top)

    text = Text(frames[0])
    text.tag_config('time', background='black', foreground='white')
    text.tag_config('title', background='gray')
    text.tag_config('algorithm', background='lightgrey')
    text.pack(fill=X, expand=TRUE, pady=5)

    text.insert('end', 'TIME: ' + run_time + '\n', 'time')
    text.insert('end', '\n')

    dict_aux = defaultdict(list)

    for key1, value1 in results.ranking.items():
        for key2, value2 in results.results.items():
            for key3, value3 in value2.items():
                if value1 == value3:
                    result = (key2, key3)
                    dict_aux[value3].append(result)

    for key1, value1 in dict_aux.items():
        path1 = key1[0].path.replace(configuration.get_directory().path, '') + '\n'
        path2 = key1[1].path.replace(configuration.get_directory().path, '')

        text.insert('end', path1 + path2 + '\n', 'title')
        text.insert('end', '\n')

        for item in value1:
            text.insert('end', item[0] + '\n', 'algorithm')
            text.insert('end', str(item[1]) + '\n')
            text.insert('end', '\n')

    Button(frames[2], text='Export', command=partial(export, window, dict_aux, run_time)).pack(padx=5, pady=5, side=LEFT)
    Button(frames[2], text='Help', command=partial(show_help, window)).pack(padx=5, pady=5, side=LEFT)
    Button(frames[2], text='Quit', command=results_top.destroy).pack(padx=5, pady=5, side=LEFT)

    results_top.mainloop()


def show_help(window):
    help_top = Toplevel(window)
    help_top.title('HELP')

    help_text = 'Coefficient obtained from each one of the selected algorithms ' + '\n' + \
                'when it was applied to compare the pair of files tokenized.'

    Label(help_top, text=help_text).pack(pady=5)
    Button(help_top, text='Quit', command=help_top.destroy).pack(pady=5)

    help_top.mainloop()


def export(window, dict_aux, run_time):
    global configuration

    export_top = Toplevel(window)
    export_top.title('EXPORT')

    path = configuration.directory + '/RESULTS'

    try:
        f = open(path, 'w')

        f.write('TIME: ' + run_time + '\n')
        f.write('\n')

        for key1, value1 in dict_aux.items():
            path1 = key1[0].path.replace(configuration.get_directory().path, '') + '\n'
            path2 = key1[1].path.replace(configuration.get_directory().path, '')

            f.write(path1 + path2 + '\n')
            f.write('\n')

            for item in value1:
                f.write(item[0] + '\n')
                f.write(str(item[1]) + '\n')
                f.write('\n')

        f.close()

        export_text = 'Results were successfully exported in\n' + path

    except:
        export_text = 'Results were not successfully exported'

    Label(export_top, text=export_text).pack(pady=5)
    Button(export_top, text='Quit', command=export_top.destroy).pack(pady=5)

    export_top.mainloop()
