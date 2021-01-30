import nltk  # Importing python natural language toolkit
from nltk.tokenize import RegexpTokenizer  # Regular Expression Tokenizer


class Parser:
    def __init__(self, is_file: bool, path: str):
        self.is_file = is_file
        self.path = path
        self.tokenizer = RegexpTokenizer(r'\w+')

    def open(self):
        if self.is_file:
            with open(self.path) as f:
                for line in f:  # For each line
                    if line.strip():  # Line is not only whitespace
                        print(self.tokenizer.tokenize(line))
            f.close()
        else:
            print('Reading from a stream')

    @staticmethod
    def setup():
        nltk.download()
        nltk.download('punkt')


def main():
    p = Parser(is_file=True, path="testinput.txt")
    # On the first run of the program, call setup and download all-corpus
    # p.setup()
    p.open()


main()
