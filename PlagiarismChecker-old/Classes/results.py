import itertools
from collections import defaultdict


def get_coefficients(results):
    dict_coefficients = defaultdict(list)

    for value1 in results.values():

        for key2, value2 in value1.items():
            dict_coefficients[value2].append(key2)

    return dict_coefficients


def get_means(results):
    dict_means = {}
    dict_coefficients = get_coefficients(results)

    for key1, value1 in dict_coefficients.items():

        mean = 0

        for item in value1:

            mean += item

        mean = round(mean / len(results), 10)

        dict_means.update({mean: key1})

    return dict_means


class Results:
    def __init__(self, dictionary):
        self.results = dictionary
        self.ranking = None

    def get_ranking(self, configuration):
        dictionary = sorted(get_means(self.results).items(), reverse=True)

        try:
            self.ranking = dict(itertools.islice(dictionary, configuration.top))

        except ValueError:
            self.ranking = dict(dictionary)
