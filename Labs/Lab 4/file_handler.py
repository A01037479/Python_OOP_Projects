"""
This module contains FileExtensions enum class, FileHandler static class and
custom exception InvalidFileTypeError
"""
import enum
from pathlib import Path


class FileExtensions(enum.Enum):
    """
    Class represents file extension .txt and .json
    """
    txt = '.txt'
    json = '.json'


class FileHandler:
    """
    Static class that manages files from reading and writing
    """
    @staticmethod
    def load_data(path, file_extension):
        """
        The method raises a various of errors and read a file from specified
        path when no error is raised.
        :param path: String
        :param file_extension: String
        :return: String
        """
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
        """
        The method append a specified line to a specified file path, creates
        the file if the file does not exist in the path.
        :param path: String
        :param lines: String
        """
        write_file = open(path, "a+")
        write_file.writelines(lines)
        write_file.close()


class InvalidFileTypeError(Exception):
    """
    Custom Error. An error to be raised when file extension given is wrong.
    """
    def __init__(self, message):
        super().__init__(message)

