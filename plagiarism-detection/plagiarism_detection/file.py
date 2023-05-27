import os

# dictionary to translate languages for the pygment lexer
languages = {
    '.java': 'java',
    '.py': 'python',
    '.js': 'javascript',
    '.sh': 'bash',
    '.bash': 'bash',
    '.cs': 'csharp',
    '.c': 'c',
    '.h': 'c',
    '.cpp': 'cpp',
    '.go': 'go',
    '.php': 'php',
    '.html': 'html',
    '.sql': 'sql',
    '.txt': 'text'
}


class File():
    """
    Class representing a source code file.
    It can store the path to the file, the source code of the file, and the 
    list containing the tokens of the source code.
    """

    def __init__(self, path="") -> None:
        self.path = path
        self.name = self.__get_name(path)
        self.language = self.__get_language(path)
        self.content = self.__get_content(path)
        self.tokens = []
    
    def set_path(self, path) -> None:
        self.path = path
    
    def set_name(self, name) -> None:
        self.name = name
    
    def set_language(self, language) -> None:
        self.language = language
    
    def set_content(self, content) -> None:
        self.content = content
    
    def set_tokens(self, tokens) -> None:
        self.tokens = tokens
    
    def get_path(self) -> str:
        return self.path
    
    def get_name(self) -> str:
        return self.name
    
    def get_language(self) -> str:
        return self.language
    
    def get_content(self) -> str:
        return self.content
    
    def get_tokens(self) -> list:
        return self.tokens
    
    @staticmethod
    def __get_name(file_path) -> str:
        """
        params:
            path (str) : the source code file path
        returns:
            str : The name of the source code file (with extension)
        """
        return os.path.split(file_path)[1]

    @staticmethod
    def __get_content(file_path) -> str:
        """
        params:
            path (str) : the source code file path
        returns:
            str : The contents of the source code file
        """
        with open(file_path, 'rb') as f:
            return f.read()
    
    @staticmethod
    def __get_language(file_path) -> str:
        """
        params:
            path (str) : the source code file path
        returns:
            str : The programming language of the source file
        """
        extension = os.path.splitext(file_path)[1]
        language = languages[extension]
        return language