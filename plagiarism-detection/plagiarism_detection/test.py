import os
import heapq
from os import listdir
from zipfile import ZipFile, is_zipfile
from pygments.token import Whitespace, Comment, Token
from algorithms import Subsequences

# import configuration settings from "config\pyproject.toml"
from config import project

root_folder = project["settings"]["root_folder"]


def find_continuous_subsequences(list1, list2, min_length=3, max_sequences=0):
    m = len(list1)
    n = len(list2)

    # Create a table to store the lengths of longest common subsequences
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # Find the length of the longest common subsequence
    for i in range(m):
        for j in range(n):
            if list1[i] == list2[j]:
                if i == 0 or j == 0:
                    table[i][j] = 1
                else:
                    table[i][j] = table[i-1][j-1] + 1
            print(table[i][j], end=" ")
        print("")


    subsequences = []
    i = 0
    while i < m:
        j = 0
        while j < n:
            # check if the length is greater than the minimum length
            if (table[i][j] >= min_length):
                # while we did not arrive at the end of a sequence we move progressively 
                # move to the end of the sequence
                while (i != m and j != n) and (table[i+1][j+1] != 0):
                    i += 1
                    j += 1

                print(i, j, table[i][j])
                
                # when we found the end of the sequence, we rebuild the sequence by backtracking trough the table
                subsequence = []
                k, l = i, j
                while (k >= 0 and l >= 0) and (table[k][l] >= 1):
                    # insert the elements at the start of the sequence
                    subsequence.insert(0, (list1[k], k, l))
                    k -= 1
                    l -= 1
                
                subsequences.append(subsequence)
            j += 1
        i += 1

    subsequences.sort(key=len, reverse=True)

    if max_sequences:
        return subsequences[:max_sequences]
    else:
        return subsequences






if __name__ == '__main__':

    # Example token lists
    list1 = [
        (Token.Punctuation, ')'),
        (Token.Keyword.Declaration, 'private'),
        (Token.Text.Whitespace, ' '),
        (Token.Name, 'Integer'),
        (Token.Text.Whitespace, ' '),
        (Token.Name.Function, 'HelloWorld'),
        (Token.Punctuation, '('),
        (Token.Punctuation, ')'),
        (Token.Text.Whitespace, ' '),
        (Token.Punctuation, '{'),
        (Token.Text.Whitespace, '\n'),
        (Token.Keyword, 'return'),
        (Token.Text.Whitespace, ' '),
        (Token.Literal.Number.Integer, '5'),
        (Token.Text.Whitespace, '\n'),
        (Token.Punctuation, '{'),
        (Token.Text.Whitespace, '\n'),
        (Token.Keyword, 'return'),
    ]

    list2 = [
        (Token.Keyword.Declaration, 'private'),
        (Token.Text.Whitespace, ' '),
        (Token.Name, 'Integer'),
        (Token.Text.Whitespace, ' '),
        (Token.Name.Function, 'HelloWorld'),
        # (Token.Punctuation, '('),
        (Token.Punctuation, ')'),
        (Token.Text.Whitespace, ' '),
        (Token.Punctuation, '{'),
        (Token.Text.Whitespace, '\n'),
        (Token.Keyword, 'return'),
        (Token.Text.Whitespace, ' '),
        (Token.Literal.Number.Integer, '10'),
        (Token.Text.Whitespace, '\n'),
        (Token.Punctuation, '{'),
        (Token.Text.Whitespace, '\n'),
        (Token.Keyword, 'return'),
    ]

    # Find the longest common sub-list
    # longest_common_subsequence = longest_subsequence(list1, list2)
    # longest_common_subsequence = longest_subsequence(list1, list2)
    # print("Longest Common Sub-list:")
    # print(longest_common_subsequence)

    # longest_common_subsequences = find_continuous_subsequences(list1, list2, 3)
    subsequences = Subsequences(list1, list2)
    eval = subsequences.jaccard_similarity()
    print(eval)
    # for seq in longest_common_subsequences:
    #     print(seq)
        # for token in seq:
        #     print(list1[token[1]] == list2[token[2]])

    # for token in longest_common_subsequence:
    #     print(token)
