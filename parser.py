import nltk                                         # Importing python natural language toolkit
from nltk.tokenize import RegexpTokenizer           # Regular Expression Tokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from spacy import *

# Used for UDP transmission / receiving
import socket


class Parser:
    def __init__(self, is_file: bool, path: str):
        self.is_file = is_file
        self.path = path
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.filtered_pos = ['CC', 'DT', 'VBZ', 'TO']
        # UDP Socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creating a TCP / IP socket
        self.server_address = ('localhost', 200)  # Tuple of address data

    def open_file(self):
        with open(self.path) as f:
            for line in f:  # For each line
                temp = self.parse_text(line)
                if temp:
                    print(temp)
        f.close()

    # def sort_text(self, input_arr):
    #     result = [10] * len(input_arr)
    #     last_was_in = False
    #     ranking = {"PRP": 1, "PRP$": 1, "NN": 2, "VB": 3, "WP": 4}
    #     print(list(map(lambda x: x[0], input_arr)))
    #     print(list(map(lambda x: x[1], input_arr)))
    #     for idx, word in enumerate(map(lambda x: x[1], input_arr)):
    #         if word == "IN":
    #             result[idx] = (0, input_arr[idx])
    #             last_was_in = True
    #             # print(result)
    #             # print("in")
    #         elif last_was_in:
    #             result[idx] = (0, input_arr[idx])
    #             last_was_in = False
    #         else:
    #             result[idx] = ranking.get(word, 10)
    #         print(result)
    #         # return sorted(result, key=lambda x: x[0])
    #     # return sorted(input_arr)
    #     # return result

    # def sort_text(self, input_arr):
    #     # (Time) Subject Verb Object
    #     print(input_arr)
    #     ranking = {
    #         "IN": 0,
    #         "PRP": 1,
    #         "PRP$": 1,
    #         "NN": 2,
    #         "NNS": 2,
    #         "NNP": 2,
    #         "NNPS": 2,
    #         "VB": 3,
    #         "VBD": 3,
    #         "VBG": 3,
    #         "VBN": 3,
    #         "VBP": 3,
    #         "VBZ": 3,
    #         "WDT": 4,
    #         "WP": 4,
    #         "WP$": 4,
    #         "WRP": 4,
    #     }
    #     result = [[]] * 6
    #     last_in = False
    #     for word, pos in input_arr:
    #         if pos != "IN":
    #             if last_in:
    #                 result[0].append(word)
    #                 last_in = False
    #             else:
    #                 result[ranking.get(pos, 5)].append(word)
    #         else:
    #             result[0].append(word)
    #             last_in = True
    #     temp = []
    #     # for arr in result:
    #     #     temp.append(arr)
    #     print(result)

    def parse_text(self, input_str: str):
        if input_str.strip():  # Line is not only whitespace
            # Tokenizes lines while removing punctuation and standardizing case
            tokens = self.tokenizer.tokenize(input_str)
            tokens = list(map(lambda x: x.lower(), tokens))
            tokens_pos = nltk.pos_tag(tokens)  # Checks parts of speech of each token
            # Filters unwanted parts of speech as well as converts back into a list of words
            filtered_tokens = filter(lambda x: x[1] not in self.filtered_pos, tokens_pos)
            print(self.sort_text(list(filtered_tokens)))

            # -------Testing code-----------
            temp = list(filtered_tokens)
            print(temp)
            # print(tokens_pos)
            # -------Testing code-----------
            filtered_tokens = map(lambda x: WordNetLemmatizer.lemmatize(x[0], 'v'), filtered_tokens)
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
    # p.start_server()
    p.open_file()


main()
