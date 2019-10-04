import enum
from pathlib import Path


class FileExtensions(enum.Enum):
    txt = '.txt'
    json = '.json'


class FileHandler:
    @staticmethod
    def load_data(path, file_extension):
        if not isinstance(path, str):
            raise TypeError('Invalid file path type!')
        if not Path(path).exists():
            raise FileNotFoundError('File path could not be found!')
        if file_extension == FileExtensions.json.value \
                or file_extension == FileExtensions.txt.value:
            file_object = open(path, "r")
            content = file_object.read()
            file_object.close()
            return content
        else:
            raise InvalidFileTypeError('File extension should be .txt or .json')

    @staticmethod
    def write_line(path, lines):
        write_file = open(path, "a+")
        write_file.writelines(lines)
        write_file.close()


class InvalidFileTypeError(Exception):
    def __init__(self, message):
        super().__init__(message)

