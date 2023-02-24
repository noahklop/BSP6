import os
import yaml
from Classes import algorithm, file, directory


def get_configuration():
    path1 = 'configuration_command.yaml'
    path2 = 'configuration_gui.yaml'

    if os.path.exists(path1):
        path = path1

    elif os.path.exists(path2):
        path = path2

    else:
        f = open('configuration.yaml', 'r')
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    f = open(path, 'r')
    data = yaml.load(f, Loader=yaml.FullLoader)
    os.remove(path)
    return data


class Configuration:
    def __init__(self):
        data = get_configuration()

        self.directory = data['directory']

        self.filename = data['name']

        if data['top']:
            self.top = data['top']

        else:
            self.top = 10

        self.algorithms = []

        for key, value in data['algorithms'].items():
            if value is True:
                algo = algorithm.Algorithm(key)
                self.algorithms.append(algo)

        if not self.algorithms:
            algo = algorithm.Algorithm('Cosine similarity')
            self.algorithms.append(algo)

        self.file_extensions = data['extensions']

        if self.directory and self.filename:
            self.file = file.File(self.directory + '/' + self.filename)

        else:
            self.file = None

    def get_directory(self):
        return directory.Directory(self.file.path.replace('.zip', ''))
