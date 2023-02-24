import time
import sys
from tkinter import *
from GUI import processing_gui, ranking_gui, configuration_gui
from Command import write_configuration_command
from Classes import configuration
from Modules import comparefiles

if __name__ == '__main__':
    # CONFIGURATION
    write_configuration_command.write(sys.argv)

    config = configuration.Configuration()

    if not config.file:
        window1 = Tk()
        window1.title('CODE PLAGIARISM CHECKER')

        configuration_gui.run(window1)

        window1.mainloop()

        config = configuration.Configuration()

    # COMPARISON
    window3 = Tk()
    window3.title('PROCESSING')

    start_time = time.time()
    processing_gui.run(window3, 'STARTING', start_time)

    # Phase 1
    directory = config.get_directory()
    processing_gui.run(window3, 'DIRECTORY OBTAINED', start_time)

    # Phase 2
    directory.recursive_unzip(config)
    processing_gui.run(window3, 'DIRECTORY UNZIPPED', start_time)

    # Phase 3
    files = directory.get_files(config)
    processing_gui.run(window3, 'FILES OBTAINED', start_time)

    # Phase 4
    for file in files:
        file.tokenize()
    processing_gui.run(window3, 'FILES TOKENIZED', start_time)

    # Phase 5
    results = comparefiles.compare(files, config)
    processing_gui.run(window3, 'ALGORITHMS APPLIED', start_time)

    # Phase 6
    results.get_ranking(config)
    run_time = processing_gui.run(window3, 'RANKING OBTAINED', start_time)

    time.sleep(1)

    window3.destroy()

    # VISUALIZATION
    window2 = Tk()
    window2.title('RANKING')

    ranking_gui.run(window2, results, run_time, config)

    window2.mainloop()

    directory.remove()

