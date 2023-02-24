import difflib
from tkinter import *
from GUI import token_diff
from functools import partial
from GUI.Frames import comparison_frames

configuration = {}


def get_file_diff(file1, file2):
    d = difflib.Differ()
    text1 = open(file1, 'r').readlines()
    text2 = open(file2, 'r').readlines()
    return d.compare(text1, text2)


def get_text(frame, file):
    global configuration
    text = Text(frame)
    text.tag_config('title', background='lightgrey')
    text.tag_config('equal', background='lime')
    text.tag_config('different')
    text.pack(side=LEFT, fill=X, expand=TRUE, pady=5)
    text.insert('end', file.replace(configuration.get_directory().path, '') + '\n\n', 'title')
    return text


def fill(text1, text2, diff, mapping):
    for item in diff:

        if item.startswith(' ') and not mapping:
            text1.insert('end', item.replace('  ', '', 1), 'equal')
            text2.insert('end', item.replace('  ', '', 1), 'equal')

        elif item.startswith('-') and not item.startswith('--- '):
            text1.insert('end', item.replace('- ', '', 1), 'different')

        elif item.startswith('+') and not item.startswith('+++ '):
            text2.insert('end', item.replace('+ ', '', 1), 'different')


def show(window, files, config):
    global configuration
    configuration = config

    path1 = files[0].path
    path2 = files[1].path

    tokens1 = files[0].tokens
    tokens2 = files[1].tokens

    diff1 = get_file_diff(path1, path2)
    diff2 = token_diff.run(tokens1, tokens2)

    top1 = Toplevel(window)
    top1.title('CODE COMPARISON')

    top2 = Toplevel(window)
    top2.title('REFORMATTED VARIABLES')

    draw_top(top1, diff1, path1, path2, False)
    draw_top(top2, diff2, path1, path2, True)

    top1.mainloop()
    top2.mainloop()


def draw_top(top, diff, path1, path2, mapping):
    frames = comparison_frames.get(top)

    text1 = get_text(frames[2], path1)
    text2 = get_text(frames[3], path2)

    fill(text1, text2, diff, mapping)

    Button(frames[4], text='Help', command=partial(show_help, top, mapping)).pack(padx=5, pady=5, side=LEFT)
    Button(frames[4], text='Quit', command=top.destroy).pack(padx=5, pady=5, side=LEFT)


def show_help(window, mapping):
    help_top = Toplevel(window)
    help_top.title('HELP')

    if mapping:
        help_text = 'List of variable names from both files which are likely to ' + '\n' + \
                    'have been reformatted to hide a plagiarism. Easy to find ' + '\n' + \
                    'similarities between both lists.'

    else:
        help_text = 'Code from both files where the lines which are an exact ' + '\n' + \
                    'match with the opposite file appear highlighted.'

    Label(help_top, text=help_text).pack(pady=5)
    Button(help_top, text='Quit', command=help_top.destroy).pack(pady=5)

    help_top.mainloop()
