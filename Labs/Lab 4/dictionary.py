from file_handler import FileExtensions, FileHandler, InvalidFileTypeError
from pathlib import PurePosixPath
import json


class Dictionary:
    def __init__(self):
        self.dict = {}

    def get_dict(self):
        return self.dict

    def load_dictionary(self, path):
        file_extension = PurePosixPath(path).suffix
        json_string = FileHandler.load_data(path, file_extension)
        self.dict = json.loads(json_string)

    def query_definition(self, word):
        definition = self.dict[word]
        print(definition)
        formatted_definition = f'{word}: {definition}\n'
        FileHandler.write_line('definitions.txt', formatted_definition)

    def is_loaded(self):
        return self.dict


def main():
    dictionary = Dictionary()
    path = "data.json"
    try:
        dictionary.load_dictionary(path)
    except FileNotFoundError as e:
        print(f'FileNotFoundError caught! {e}')
    except InvalidFileTypeError as e:
        print(f'InvalidFileTypeError caught! {e}')
    else:
        go = True
        while go:
            word = input('Enter a word: ')
            if word == 'exitprogram':
                go = False
            if word not in dictionary.get_dict().keys():
                print('No such word in dictionary.\n')
                continue
            else:
                print(dictionary.query_definition(word))


if __name__ == '__main__':
    main()
