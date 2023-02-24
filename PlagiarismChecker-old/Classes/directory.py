import os
import shutil
import fnmatch
from Classes import file


# Method to find paths with a specific pattern and return it
def find(pattern, path):
    result = []

    for root, dirs, files in os.walk(path):

        for name in files:

            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))

    return result


class Directory:
    def __init__(self, path):
        self.path = path

    def remove(self):
        if os.path.exists(self.path + '.zip'):
            shutil.rmtree(self.path)

    def get_files(self, configuration):
        extensions = configuration.file_extensions
        files = []

        if extensions:
            for extension in extensions:
                for fil in find('*.' + extension, self.path):
                    fi = file.File(fil)
                    if fi.language:
                        files.append(fi)

        else:
            for fil in find('*.*', self.path):
                fi = file.File(fil)
                if fi.language:
                    files.append(fi)

        return files

    def recursive_unzip(self, configuration):
        if '.zip' in configuration.file.path:
            configuration.file.unzip()

        for fil in find('*.zip', self.path):
            fi = file.File(fil)
            fi.unzip()
            fi.remove()

