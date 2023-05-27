from config import project

import webbrowser, os
from simple_term_menu import TerminalMenu

from pre_processing import pre_process, tokenize_files, pre_process_tokens
from directory import Directory
from eval import evaluate_files, save_results

def menu(files):
    done = False
    options = ["Quit"] + [f"similar_files_{i+1}: {files[i][1]}" for i in range(len(files))]
    terminal_menu = TerminalMenu(options)
    while not done:
        menu_entry_index = terminal_menu.show()
        if menu_entry_index == 0:
            done = True
        else:
            html_file = files[menu_entry_index-1][0]     # index -1 because te first one is QUIT
            webbrowser.open_new_tab('file://' + html_file)

def run():
    dir = Directory()
    files = dir.get_files()

    # pre-process the files
    pre_process(files)
    # tokenize the file contents
    tokenize_files(files)
    # re-process the files to remove other parts specified inside the config file
    pre_process_tokens(files)
    
    # get similarity
    results = evaluate_files(files)
    html_files = save_results(results)

    # Open menu to open html file comparison
    print("")
    print("Choose a file you want to display: ")
    menu(html_files)

if __name__ == '__main__':
    run()

