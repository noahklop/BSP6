import re
from pygments import lex
from pygments.lexers import get_lexer_by_name
from pygments.token import Whitespace, Comment, Token

# import configuration settings from "config\pyproject.toml"
from config import project, MissingParameter

from file import File


def remove_obsolete_code(source_code) -> str:
    """
    Removes all parts of code that are specified in the 'obsolete_code' list in the config file 

    params:
        source_code (str): string containing the source code from one file
        
    returns:
        source_code (str): string containing the UPDATED source code from one file
    """
    # remove all the obsolete code parts
    for regex in project["settings"]["pre_processing"]["obsolete_code"]:
        # we have to decode the source code to use regex
        try:
            source_code = re.sub(regex, '', source_code)
        except Exception as e:
            raise MissingParameter("settings.pre_processing", e)
    
    # then we encode the source code back to bytes
    return source_code.encode('utf-8')

def remove_imports(source_code) -> str:
    """
    Removes all the import statements from the source code

    params:
        source_code (str): string containing the source code from one file
        
    returns:
        source_code (str): string containing the UPDATED source code from one file
    """
    regex = r"import\s+[\w.]+(?:\*|[\w.]+);\s*"
    source_code = re.sub(regex, '', source_code.decode('utf-8', errors='ignore'))

    return source_code.encode('utf-8')


def remove_multi_spaces(source_code) -> str:
    """
    Removes multiple white spaces and new lines

    params:
        source_code (str): string containing the source code from one file

    returns:
        source_code (str): string containing the UPDATED source code from one file
    """
    
    # decode the source code
    source_code = source_code.decode('utf-8')

    # remove tabs and multiple blank spaces
    source_code = re.sub(r' {4}', '', source_code)
    source_code = re.sub(r' +', ' ', source_code)
    # remove multiple new lines
    source_code = re.sub(r'\n\s*\n', '\n\n', source_code)

    # encode and return the source code
    return source_code.encode('utf-8')


# def find_common_code(files_list):
#     """

#     params:
#         files_list (list): list containing paths to all the source code files
#     returns:
#         common_code (list): list of all source code lines that are common between all files
#     """
#     common_code = []
#     return common_code

# def remove_common_code(file):
#     pass


# def clean_files(dir) -> None:
#     """
#     Function that takes a Directory as input and cleans the contents of the Files inside that Directory

#     params:
#         dir (Directory): Directory containing the  Files

#     returns:
#         None
#     """
#     for file in dir.get_files():
#         # get the contents of the file
#         source_code = file.get_content()
        
#         # pre-process source code according to configuration settings
#         source_code = remove_obsolete_code(source_code)
#         if project["settings"]["ignore_multi_spaces"]:
#             source_code = remove_multi_spaces(source_code)

#         # save the modified source code back into the File
#         file.set_content(source_code)


def pre_process(files) -> None:
    """
    Function that takes a list of Files as input and cleans the contents of the Files inside that Directory

    params:
        files (list): list containing the Files

    returns:
        None : cleans and updates the source_code of all the input files
    """
    for file in files:
        # get the contents of the file
        source_code = file.get_content().decode('utf-8', errors='ignore')
        # pre-process source code according to configuration settings
        source_code = remove_obsolete_code(source_code)
        if project["settings"]["pre_processing"]["ignore_multi_spaces"]:
            source_code = remove_multi_spaces(source_code)
        if project["settings"]["pre_processing"]["ignore_imports"]:
            source_code = remove_imports(source_code)

        # save the modified source code back into the File
        file.set_content(source_code)


def tokenize_file(file) -> None:
    """
    Tokenize the source code from a File using Pygments.

    params:
        file (File): The File instance containing the source code that should be tokenized.
        
    returns:
        None : creates and saves the tokens of the input file
    """
    # get the language of the file
    language = file.get_language()

    # get the contents of the file
    source_code = file.get_content()

    # Get lexer for the specified language
    lexer = get_lexer_by_name(language)

    # Tokenize the source code using the lexer
    tokens = lex(source_code, lexer)

    # Extract tokens
    token_list = list(tokens)

    file.set_tokens(token_list)


def tokenize_files(files) -> None:
    """
    Tokenize the source code from all the Files inside the input list.

    params:
        files (list): list of File instances containing the source code that should be tokenized.
        
    returns:
        None : creates and saves the tokens of all the input files
    """
    for file in files:
        tokenize_file(file)


def remove_multi_whitespaces(file) -> None:
    """
    Remove all the Token.Text.Whitespace tokens from the input File
    
    params:
        file (File) : File containing list of pygments Tokens

    returns:
        None : updates the tokens of the input file
    """

    updated_tokens = []
    nl_counter = 0
    space_counter = 0
    for token in file.get_tokens():
        # see if token is correct type

        if token[1] == '\n':
            # reset space counter
            space_counter = 0
            # check if its the first one
            if nl_counter == 0:
                updated_tokens.append(token)
            nl_counter += 1

        elif token[1] == ' ':
            # reset new line counter
            nl_counter = 0
            # check if its the first one
            if space_counter == 0:
                updated_tokens.append(token)
            space_counter += 1
        
        else:
            # reset counters
            nl_counter = 0
            space_counter = 0
            updated_tokens.append(token)
            
    file.set_tokens(updated_tokens)


def remove_whitespaces(file) -> None:
    """
    Remove all the Token.Text.Whitespace tokens from the input File
    
    params:
        file (File) : File containing list of pygments Tokens

    returns:
        None : updates the tokens of the input file
    """

    updated_tokens = []
    for token in file.get_tokens():
        # see if token is correct type
        if token[0] not in Whitespace:
            # add the token to the new list
            updated_tokens.append(token)
    
    file.set_tokens(updated_tokens)


def remove_comments(file) -> None:
    """
    Remove all the Token.Comment tokens from the input File
    
    params:
        file (File) : File containing list of pygments Tokens

    returns:
        None : updates the tokens of the input file
    """

    updated_tokens = []
    for token in file.get_tokens():
        # print(token[0], (token[0] == Whitespace))
        # see if token is correct type
        if token[0] not in Comment:
            # add the token to the new list
            updated_tokens.append(token)
    
    file.set_tokens(updated_tokens)


def pre_process_tokens(files) -> None:
    """
    Remove all the tokens matching the Token types specified in the configuration file
    
    params:
        files (list) : list containing the Files to be treated

    returns:
        None : updates the tokens of the input file
    """
    for file in files:
        if project["settings"]["pre_processing"]["ignore_multi_spaces"]:
            remove_multi_whitespaces(file)
        if project["settings"]["pre_processing"]["ignore_comments"]:
            remove_comments(file)


if __name__ == '__main__':
    file = File("/Users/noahk/Documents/Uni.lu/Semester_6/BSP6/plagiarism-detection/java_files/test1.java")
    print(file.get_name())
    tokens = tokenize_file(file)
    print(file.get_tokens())
