import re
import os
import sys
from os import listdir
from zipfile import ZipFile, is_zipfile
from shutil import copytree

# import configuration settings from "config\pyproject.toml"
from config import project, MissingParameter

from file import File


class Directory():
    def __init__(self, root_folder='config') -> None:
        """
        Class representing the folder containing the source code files.
        If the root_folder parameter is not given, the path specified in
        the config file will be used.

        params:
            root_folder (str)(optional) : path to directory containing source code files
        returns:
            Instance of type Directory
        """
        # check if a path has been provided
        if root_folder == 'config':
            root_folder = project["settings"]["file_handling"]["root_folder"]
            
        # create copy of root folder if specified in config
        if project["settings"]["file_handling"]["create_folder_copy"]:
            self.target_folder = root_folder + '-copy'
            copytree(root_folder, self.target_folder, dirs_exist_ok=True)
        else:
            # Do a safety check
            safety_check = str(input("WARNING: create_folder_copy = false \nPlease set this setting to true, else the original working directory will be manipulated! \nDo you want to continue anyway? (y/n) "))
            passed = False
            while not passed:
                if safety_check in ['n', 'N', 'no', 'No'] :
                    exit()
                elif safety_check == ['y', 'Y']:
                    self.target_folder = root_folder
                    passed = True
                else:
                    str(input("Please enter 'y' for yes or 'n' for no: "))

        self.files = self.__get_source_files(self.target_folder)
    
    def get_files(self) -> list:

        return self.files

    def extract_zip_files(self) -> None:
        """
        Recursively loops through all the files in the subfolders of 'target_folder'
        and extracts all the zip files that are found.

        params:
            None
        returns:
            None
        """

        # recursively loop trough all files / sub-directories in root folder
        for (dirpath, dirnames, filenames) in os.walk(self.target_folder):
            for file in filenames:
                # check if file is a zip archive
                if file.endswith(".zip"):
                    with ZipFile(os.path.join(dirpath, file)) as item: # treat the file as a zip
                        # get .zip file name without extension
                        new_dirname = os.path.splitext(file)[0]
                        # extract files in new folder with same name as .zip file
                        item.extractall(os.path.join(dirpath, new_dirname))
                    # delete zip file if specified in config
                    if project["settings"]["file_handling"]["delete_zip"]:
                        os.remove(os.path.join(dirpath, file))

    @staticmethod
    def __get_source_files(target_folder) -> list:
        """
        Recursively loops through all the files in the subfolders of 'target_folder'
        and puts them in the 'files' list if they are source-code files specified in the config.

        params:
            None
        returns:
            list of Files containing source code file paths
        """

        files = []
        # recursively loop trough all files / sub-directories in target_folder
        for (dirpath, dirnames, filenames) in os.walk(target_folder):
            for file in filenames:
                # check if the file has the correct extension
                extension = os.path.splitext(file)[1]
                if extension in project["settings"]["file_handling"]["extensions"]:
                    # check if file name matches filename that should be ignored (config)
                    if not any([re.match(pattern, file) for pattern in project["settings"]["file_handling"]["ignore_files"]]):
                        filepath = os.path.join(dirpath, file)
                        # Create instance of type File and store the path
                        f = File(path=filepath)
                        # add the files to the list
                        files.append(f)

        return files


if __name__ == '__main__':
    dir = Directory()
    # dir.extract_zip_files()
    dir.get_files()
    print(len(dir.files))

    for file in dir.files:
        print("name:", file.get_name(), "language:", file.get_language())
