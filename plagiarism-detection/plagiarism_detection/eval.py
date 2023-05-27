from config import project, MissingParameter

import os, shutil, csv
from openpyxl import Workbook
from itertools import combinations
from difflib import SequenceMatcher
from tqdm import tqdm

from algorithms import Ngram, Subsequences


def apply_similarity_algorithm(tokens1, tokens2) -> float:
    """
    function that applies the correct similarity detection algorithm based on the settings in the config file

    params:
        tokens1 (list): List of tokens from the first input file.
        tokens2 (list): List of tokens from the second input file.
    returns:
        (float) : the evaluation score
    """

    if project["settings"]["algorithms"]["N-Gram"]:
        # check if N was specified inside the config file
        if type(project["settings"]["algorithms"]["N-Gram"]) == int:
            ngram = Ngram(tokens1, tokens2, project["settings"]["algorithms"]["N-Gram"])
        else:
            ngram = Ngram(tokens1, tokens2)
        result = ngram.jaccard_similarity()
    elif project["settings"]["algorithms"]["Needleman-Wunsch"]:
        matcher = SequenceMatcher(a=tokens1, b=tokens2)
        result = matcher.ratio()
    elif project["settings"]["algorithms"]["Subsequences"]:
        # check if minimum length was specified inside the config file
        if type(project["settings"]["algorithms"]["Subsequences"]) == int:
            subseq = Subsequences(tokens1, tokens2, project["settings"]["algorithms"]["Subsequences"])
        else:
            subseq = Subsequences(tokens1, tokens2)
        result = subseq.jaccard_similarity()
    else:
        raise MissingParameter("settings.algorithms")
    
    return result


def add_color_field(tokens1, tokens2):
    """
    function to add the color field to the tokens

    params:
        tokens1 (list): List of tokens from the first input file.
        tokens2 (list): List of tokens from the second input file.
    returns:
        (token), (token) : token = (Token, #color)
    """
    new_tokens1 = []
    new_tokens2 = []

    for token in tokens1:
        # set color value to white
        new_tokens1.append((token, "none"))
    
    for token in tokens2:
        # set color value to white
        new_tokens2.append((token, "none"))
    
    return new_tokens1, new_tokens2


def prepare_for_coloring(file1, file2):
    """
    function to set the color field of the tokens to the correct value

    params:
        file1 (list): first input file.
        file2 (list): input file.
    returns:
        (token), (token) : token = (Token, #color)
    """
    # get tokens with initialized color field
    tokens1, tokens2 = add_color_field(file1.tokens, file2.tokens)
    ss = Subsequences(file1.tokens, file2.tokens)
    subsequences = ss.find_common_subsequences(coloring=True)
    for seq in subsequences:
        for common_token in seq:
            # extract token content
            (token, i, j, color) = common_token
            # set color to new value
            tokens1[i] = (tokens1[i][0], color)
            tokens2[j] = (tokens2[j][0], color)
    
    return tokens1, tokens2


def evaluate_files(files) -> list:
    """
    Function that takes the list of files as input and returns a sorted list of the evaluation results.

    params:
        files (list) : list containing the input Files
    returns:
        (list) : list of tuples (file1.name, file2.name, similarity_metric)
    """

    # create all possible file combinations (r is the number of files per combination)
    file_combinations = combinations(files, r=2)
    evaluation = []
    iterations = len(files)*(len(files)-1)//2
    for (file1, file2) in tqdm(file_combinations, total=iterations):
        tokens1 = file1.tokens
        tokens2 = file2.tokens
        metric = apply_similarity_algorithm(tokens1, tokens2)
        evaluation.append((file1, file2, round(metric, 4)))
        # print(f"pair: ({file1.name}, {file2.name}) : {out}")
    
    evaluation.sort(key=lambda tup: tup[2], reverse=True)

    return evaluation


def save_result(result, save_location, rank) -> str:
    """
    We save each high-similarity pair inside a folder. Each file should be saved as a .txt file with all the similar code highlighted.

    params:
        result (tuple) : (File1, File2, metric)
        save_location (str) : parent folder path ('.../results') to store the results at
        rank (int) : the rank of the compared files
    returns:
        (str) : the path to the html file
    """

    (file1, file2, metric) = result

    colored_tokens1, colored_tokens2 = prepare_for_coloring(file1, file2)

    # create the folder to store the .txt files in
    path = os.path.join(save_location, f"similar_files_{rank}")
    os.mkdir(path)

    # create the html file
    file_path = os.path.join(path, file1.name + "+" + file2.name + '.html')
    with open(file_path, 'w') as f:
        f.write(f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body style="margin: 0px;">
<h3 style='margin-left: 1rem;'>The similarity between the two files is {str(round(metric * 100, 2))}%</h3>
<div style='display: flex; flex-direction: row;'>
''')
        # file1
        f.write(f'<div style="padding: 1rem; background-color: #222222; width: 49vw; min-height: 100vh; border-right: 2px solid #000000;">\n')
        for token in colored_tokens1:
            if token[0][1] == '\n':
                f.write('\n<br>\n')
            elif token[0][1] == ' ':
                f.write(' ')
            else:
                f.write(f'<span style="background-color: {token[1]}; color: #E8E8E8;"> {token[0][1]} </span>')
        f.write('</div>')

        # file2
        f.write(f'<div style="padding: 1rem; background-color: #222222; width: 49vw; min-height: 100vh; border-left: 2px solid #000000;">\n')
        for token in colored_tokens2:
            if token[0][1] == '\n':
                f.write('\n<br>\n')
            elif token[0][1] == ' ':
                f.write(' ')
            else:
                f.write(f'<span style="background-color: {token[1]}; color: #E8E8E8;"> {token[0][1]} </span>')
        f.write('</div>')

        f.write(f'</div></body></html>')
    
    return file_path


def save_results(results: list):
    """
    saves the top results inside a newly created 'result' folder at the location specified inside the config

    params: 
        results (list) : list of results (File1, File2, metric)
    returns:
        (list) : list containing the paths to the html files
    """
    # create folder to store the results
    path = os.path.join(project["settings"]["eval"]["save_location"], "results")
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

    if project["settings"]["eval"]["create_results_csv"] or project["settings"]["eval"]["create_results_excel"]:
        # save all the results inside a csv file
        csv_path = os.path.join(path, "all_results.csv")
        with open(csv_path, mode='w') as result_file:
            result_writer = csv.writer(result_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for result in results:
                (file1, file2, metric) = result
                result_writer.writerow([file1.name, file2.name, metric])

        # save all the results inside an excel sheet
        if project["settings"]["eval"]["create_results_excel"]:
            xlsx_path = os.path.join(path, "all_results.xlsx")
            wb = Workbook()
            ws = wb.active
            with open(csv_path, 'r') as f:
                for row in csv.reader(f):
                    ws.append(row)
            wb.save(xlsx_path)

    # save the top results
    i = 0
    html_paths = []
    max_results = project["settings"]["eval"]["max_results"]
    if max_results >= 1:
        for res in results[:max_results]:
            i += 1
            print('{:30.30} {:30.30} {:7.7} '.format(res[0].name, res[1].name, str(res[2])))
            # print(res[0].name, res[1].name, str(res[2])))
            html_path = save_result(res, path, i)
            html_paths.append((html_path, res[2]))
        
        return html_paths
    else:
        raise MissingParameter("settings.eval.max_results", "Must be >= 1")