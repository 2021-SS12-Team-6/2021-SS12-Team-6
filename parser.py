import nltk                                 # Importing python natural language toolkit
from nltk.tokenize import RegexpTokenizer   # Regular Expression Tokenizer
from stopwords import get_stopwords

# Used for UDP transmission / receiving
import socket
# from threading import Thread


class Parser:
    def __init__(self, is_file: bool, path: str):
        self.is_file = is_file
        self.path = path
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.stopwords = get_stopwords('english')
        self.filtered_pos = ['CC', 'DT', 'VBP', 'VBZ']
        # UDP Socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creating a TCP / IP socket
        self.server_address = ('localhost', 200)  # Tuple of address data

    def open_file(self):
        with open(self.path) as f:
            for line in f:  # For each line
                print(self.parse_text(line))
        f.close()

    def parse_text(self, input_str: str):
        if input_str.strip():  # Line is not only whitespace
            # Tokenizes lines while removing punctuation and standardizing case
            tokens = self.tokenizer.tokenize(input_str)
            tokens = list(map(lambda x: x.lower(), tokens))
            # tokens = list(filter(lambda x: x not in self.stopwords, tokens))
            tokens_pos = nltk.pos_tag(tokens)  # Checks parts of speech of each token
            # Filters unwanted parts of speech as well as converts back into a list of words
            filtered_tokens = filter(lambda x: x[1] not in self.filtered_pos, tokens_pos)
            # -------Testing code-----------
            # temp = list(filtered_tokens)
            # print(temp)
            # print(tokens_pos)
            # -------Testing code-----------
            filtered_tokens = map(lambda x: x[0], filtered_tokens)
            # Prints filtered list
            temp = list(filtered_tokens)
            if temp:
                return temp

    def start_server(self):
        print(f'Starting server on {self.server_address[0]} port {self.server_address[1]}')
        self.sock.bind(self.server_address)
        self.listen(True)

    def listen(self, cont: bool):
        while cont:
            print('Waiting for message')
            data, address = self.sock.recvfrom(4096)
            print(f"\nReceived {len(data)} bytes from {address}")
            if data:
                data = data.decode(encoding="utf-8")
                processed_data = " ".join(self.parse_text(data)).encode()
                sent = self.sock.sendto(processed_data, address)
                print(f"Sent {sent} bytes to {address}")

    @staticmethod
    def setup():
        nltk.download()
        nltk.download('punkt')  # Punctuation
        nltk.download('averaged_perceptron_tagger')  # Used for parts of speech

    def close(self):
        self.listen(False)


def main():
    p = Parser(is_file=True, path="testinput.txt")
    # On the first run of the program, call setup and download all-corpus
    # p.setup()
    p.start_server()
    # p.open_file()


main()
