"""

"""
import sys
from difflib import get_close_matches
from file_handler import FileExtensions, FileHandler, InvalidFileTypeError
from pathlib import PurePosixPath
import json


class Dictionary:
    def __init__(self):
        self.dict = {}

    def get_dict(self):
        return self.dict

    def load_dictionary(self, path):
        try:
            file_extension = PurePosixPath(path).suffix
            json_string = FileHandler.load_data(path, file_extension)
            self.dict = json.loads(json_string)
        except FileNotFoundError as e:
            print(f'FileNotFoundError caught! {e}')
        except InvalidFileTypeError as e:
            print(f'InvalidFileTypeError caught! {e}')
        except TypeError as e:
            print(f'TypeError caught! File name should be {e}')
        except json.decoder.JSONDecodeError:
            print(f"Wrong format dictionary! Content has to be JSON.")

    def query_definition(self, word):
        try:
            definition = self.dict[word]
        except KeyError:
            try:
                definition = self.dict[word.lower()]
            except KeyError:
                try:
                    definition = self.dict[word.upper()]
                except KeyError:
                    try:
                        definition = self.dict[word.capitalize()]
                    except KeyError:
                        print('No match word!')
                        close_matches = get_close_matches(word, self.dict.keys())
                        if close_matches:
                            print('Closed matches: ')
                            for x in range(len(close_matches)):
                                print(f'{x+1}.{close_matches[x]}')
                    else:
                        self.print_and_write(word, definition)
                else:
                    self.print_and_write(word, definition)
            else:
                self.print_and_write(word, definition)
        else:
            self.print_and_write(word, definition)

    @staticmethod
    def print_and_write(word, definition):
        print(definition)
        formatted_definition = f'{word}: {definition}\n'
        FileHandler.write_line('definitions.txt', formatted_definition)

    def is_loaded(self):
        return self.dict


def main():
    dictionary = Dictionary()
    path_input = input('Enter file path: ')
    path = path_input
    dictionary.load_dictionary(path)
    if dictionary.is_loaded():
        print("Dictionary loaded!")
    else:
        print("Unable to load dictionary")
        sys.exit()

    go = True
    while go:
        word = input('Enter a word: ')
        if not word == 'exitprogram':
            dictionary.query_definition(word)
            continue
        go = False


if __name__ == '__main__':
    main()
