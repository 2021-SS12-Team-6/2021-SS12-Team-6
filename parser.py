import nltk                                 # Importing python natural language toolkit
from nltk.tokenize import RegexpTokenizer   # Regular Expression Tokenizer
from stopwords import get_stopwords


class Parser:
    def __init__(self, is_file: bool, path: str):
        self.is_file = is_file
        self.path = path
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.stopwords = get_stopwords('english')
        self.filtered_pos = ['CC', 'DT', 'VBP', 'VBZ']

    def open(self):
        if self.is_file:
            with open(self.path) as f:
                for line in f:  # For each line
                    if line.strip():  # Line is not only whitespace
                        # Tokenizes lines while removing punctuation and standardizing case
                        tokens = self.tokenizer.tokenize(line)
                        tokens = list(map(lambda x: x.lower(), tokens))
                        # tokens = list(filter(lambda x: x not in self.stopwords, tokens))
                        tokens_pos = nltk.pos_tag(tokens)  # Checks parts of speech of each token
                        # Filters unwanted parts of speech as well as converts back into a list of words
                        filtered_tokens = filter(lambda x: x[1] not in self.filtered_pos, tokens_pos)
                        # -------Testing code-----------
                        temp = list(filtered_tokens)
                        print(temp)
                        # print(tokens_pos)
                        # -------Testing code-----------
                        # filtered_tokens = map(lambda x: x[0].lower(), filtered_tokens)
                        # Prints filtered list
                        temp = list(filtered_tokens)
                        if temp:
                            print(temp)
            f.close()
        else:
            print('Reading from a stream')

    @staticmethod
    def setup():
        nltk.download()
        nltk.download('punkt')  # Punctuation
        nltk.download('averaged_perceptron_tagger')  # Used for parts of speech


def main():
    p = Parser(is_file=True, path="testinput.txt")
    # On the first run of the program, call setup and download all-corpus
    # p.setup()
    p.open()


main()
