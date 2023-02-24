import textdistance


algorithms = {
    'Cosine similarity': 'cosine',
    'Bag distance': 'bag',
    'Jaccard index': 'jaccard',
    'Tversky index': 'tversky',
    'Sørensen–Dice coefficient': 'sorensen',
    'Overlap coefficient': 'overlap',
    'Tanimoto distance': 'tanimoto'
}


def apply_bag(tokens1, tokens2):
    difference = textdistance.bag(tokens1, tokens2)

    if len(tokens1) >= len(tokens2):
        distance = (len(tokens1) - difference) / len(tokens1)

    else:
        distance = (len(tokens2) - difference) / len(tokens2)

    return distance


class Algorithm:
    def __init__(self, name):
        self.name = name
        self.method = algorithms[name]

    def apply(self, tokens1, tokens2):
        if len(tokens1) == 0 or len(tokens2) == 0:
            distance = 0

        elif self.name == 'Bag distance':
            distance = apply_bag(tokens1, tokens2)

        else:
            distance = getattr(textdistance, self.method)(tokens1, tokens2)

        return distance



