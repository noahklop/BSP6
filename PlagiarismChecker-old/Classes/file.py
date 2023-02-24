import os
import re
import zipfile
import pygments
from pygments.token import Token
from pygments.util import ClassNotFound
from pygments.lexers import get_lexer_for_filename


parsed_tokens = [Token.Keyword, Token.Literal.String, Token.Name.Constant,
                 Token.Literal.Number, Token.Name.Decorator, Token.Operator, Token.Operator.Word,
                 Token.Name.Function, Token.Name.Namespace, Token.Name.Variable.Instance,
                 Token.Name.Variable.Class, Token.Comment.Single
                 ]


class File:
    def __init__(self, path):
        self.path = path
        self.tokens = []

        try:
            self.language = get_lexer_for_filename(self.path)

        except ClassNotFound:
            self.language = None

    def remove(self):
        os.remove(self.path)

    def unzip(self):
        new_path = self.path.replace('.zip', '')
        zip_converter = zipfile.ZipFile(self.path, 'r')
        zip_converter.extractall(new_path)
        zip_converter.close()

    def tokenize(self):
        try:
            lines = open(self.path, 'r').readlines()

            for line in lines:

                for token in pygments.lex(line, self.language):

                    if token[0] in parsed_tokens:
                        print("t0 =", token[0], "  t1 =", token[1])
                        self.tokens.append(token)

        except:
            pass

    def get_tokens(self):
        split_tokens = []

        for token in self.tokens:
            split_tokens.append(token[0])
            split_tokens.append(token[1])

        return split_tokens

    def get_student(self, configuration):
        dir = configuration.get_directory().path
        path = self.path.replace(dir + '/', '')
        student = re.sub('\/.*', '', path)
        return student

    def different(self, file, configuration):
        if self.get_student(configuration) != file.get_student(configuration):
            return True

        else:
            return False
