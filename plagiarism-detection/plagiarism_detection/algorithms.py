import os, binascii, random

from config import project, MissingParameter

color_palette = [
    "#2f4f4f60",
    "#a52a2a60",
    "#2e8b5760",
    "#80800060",
    "#80008060",
    "#ff000060",
    "#ff8c0060",
    "#ffd70060",
    "#00ff7f60",
    "#4169e160",
    "#00bfff60",
    "#0000ff60",
    "#adff2f60",
    "#ff00ff60",
    "#f0e68c60",
    "#ff149360",
    "#ffa07a60",
    "#ee82ee60",
    "#7fffd460"
]

class Ngram():

    def __init__(self, tokens1, tokens2, n=3) -> None:
        self.tokens1 = tokens1
        self.tokens2 = tokens2
        self.n = n
    
    def create_token_ngrams(self, tokens) -> list:
        """
        Creates ngrams from only the tokens (not the actual code unit value)
        Example: 
            The input tokens are tuples of the form (Token, 'value')
            This function creates the ngrams from only the Token part of the tuple.

        params:
            tokens (tuple) : Token tuple (Token, 'value')
            n (int) : the N-gram value
        returns:
            ngrams (list) : A list of all possible N-gram tuples
        """

        tokens = [token for (token, _) in tokens]
        ngrams = []

        for i in range(len(tokens) - self.n + 1):
            ngram = tokens[i:i+self.n]
            ngrams.append(tuple(ngram))

        return ngrams
    
    def create_string_ngrams(self, tokens) -> list:
        """
        Creates ngrams from only the values (not the actual code unit value)
        Example: 
            The input tokens are tuples of the form (Token, 'value')
            This function creates the ngrams from only the 'value' part of the tuple.

        params:
            tokens (tuple) : Token tuple (Token, 'value')
            n (int) : the N-gram value
        returns:
            ngrams (list) : A list of all possible N-gram tuples
        """

        tokens = [value for (_, value) in tokens]
        ngrams = []

        for i in range(len(tokens) - self.n + 1):
            ngram = tokens[i:i+self.n]
            ngrams.append(ngram)

        return ngrams
    
    def jaccard_similarity(self) -> float:
        """
        Calculates the Jaccard similarity coefficient between two sets of token n-grams.

        params (indirect):
            self.tokens1 (list): List of tokens from the first input.
            self.tokens2 (list): List of tokens from the second input.

        returns:
            float: Jaccard similarity coefficient between the two sets of token n-grams.
        """

        ngrams1 = self.create_token_ngrams(self.tokens1)
        ngrams2 = self.create_token_ngrams(self.tokens2)
        set1 = set(ngrams1)
        set2 = set(ngrams2)
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))

        return intersection / union


class Subsequences():

    def __init__(self, list1, list2, min_length=5) -> None:
        self.list1 = list1
        self.list2 = list2
        self.min_length = min_length

    def find_common_subsequences(self, max_sequences=0, coloring=False) -> list:
        """
        Function that takes two lists and finds all the common subsequences between those two lists.

        params:
            list1 (list) : first sequence to be compared
            list2 (list) : second sequence to be compared
            min_length (int) : the minimum length of the subsequences
            max_sequences (int) : the maximum number of subsequences to be returned

        returns:
            sunsequences (list) : all the subsequences in order of their length (largest to shortest)
        """

        m = len(self.list1)
        n = len(self.list2)

        # Create a table to store the lengths of common subsequences
        table = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the table
        for i in range(m):
            for j in range(n):
                if project["settings"]["eval"]["compare_token"] == 'type':
                    token1 = self.list1[i][0]
                    token2 = self.list2[j][0]
                elif project["settings"]["eval"]["compare_token"] == 'value':
                    token1 = self.list1[i]
                    token2 = self.list2[j]
                else:
                    raise MissingParameter('settings.eval.compare_token', "Must be 'value' or 'token'.")
                # check if token type is the same
                if token1 == token2:
                    if i == 0 or j == 0:
                        table[i][j] = 1
                    else:
                        table[i][j] = table[i-1][j-1] + 1
            #     print(table[i][j], end=" ")
            # print("")

        used_tokens = []
        subsequences = []
        i = 0
        while i < m:
            j = 0
            while j < n:
                # check if the length is greater than the minimum length
                if (table[i][j] >= self.min_length):
                    # while we did not arrive at the end of a sequence we move progressively 
                    # move to the end of the sequence
                    while (i != m and j != n) and (table[i+1][j+1] != 0):
                        i += 1
                        j += 1
                    
                    # print(i, j, table[i][j])
                    
                    # when we found the end of the sequence, we build the sequence by backtracking trough the table
                    if coloring:
                        color = random.choice(color_palette)
                    else:
                        color = "none"
                    subsequence = []
                    k, l = i, j
                    # check if not at border or beginning of sequence or used token
                    while (k >= 0 and l >= 0) and (table[k][l] >= 1) and not(l in used_tokens):
                        # add the j index to the used token list so we do not use it again
                        # print()
                        used_tokens.append(l)
                        # insert the elements at the start of the sequence
                        subsequence.insert(0, (self.list1[k], k, l, color))
                        k -= 1
                        l -= 1
                    
                    subsequences.append(subsequence)
                    j = n
                j += 1
            i += 1

        # sort the sequences by length from longest to shortest
        subsequences.sort(key=len, reverse=True)

        # check if max_length was provided
        if max_sequences:
            return subsequences[:max_sequences]
        else:
            return subsequences
        

    # evaluation metric for the find_common_subsequences method
    def jaccard_similarity(self) -> float:
        """
        Calculates the Jaccard similarity coefficient between two sequences.

        params:
            list1 (list) : first sequence to be compared
            list2 (list) : second sequence to be compared
            sunsequences (list) : all the common subsequences of the two lists
        returns:
            float: Jaccard similarity coefficient between the two lists.
        """

        # get the subsequences
        subsequences = self.find_common_subsequences()

        # get number of common elements
        common = sum([len(seq) for seq in subsequences])
        # get number of unique elements of list1
        unique_list1 = len(self.list1) - common
        # get number of unique elements of list2
        unique_list2 = len(self.list2) - common
        # get number of elements in union
        union = unique_list1 + unique_list2 + common

        # get the metric
        metric = common / union

        return metric