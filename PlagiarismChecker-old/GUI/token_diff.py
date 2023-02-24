import difflib
from pygments.token import Token


def run(tokens1, tokens2):
    d = difflib.Differ()
    text1 = ''
    text2 = ''
    lookup1 = set()
    lookup2 = set()
    tokens1 = [x for x in tokens1 if x not in lookup1 and lookup1.add(x) is None]
    tokens2 = [x for x in tokens2 if x not in lookup2 and lookup2.add(x) is None]

    for token1, token2 in zip(tokens1, tokens2):
        if token1[0] is Token.Name:
            text1 += token1[1] + '\n'

        if token2[0] is Token.Name:
            text2 += token2[1] + '\n'

    diff = d.compare(text1.splitlines(keepends=True), text2.splitlines(keepends=True))

    return get_mapping(diff)


def get_mapping(diff):
    d = difflib.Differ()
    text1 = ''
    text2 = ''
    diff_list = []

    # Remove elements in both lists to avoid green background
    for item in diff:

        if not item.startswith(' '):
            diff_list.append(item)

    for item in diff_list:

        if item.startswith('-'):
            text1 += item.replace('- ', '', 1)

        elif item.startswith('+'):
            text2 += item.replace('+ ', '', 1)

    diff = d.compare(text1.splitlines(keepends=True), text2.splitlines(keepends=True))

    return diff


