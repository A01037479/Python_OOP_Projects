"""
This module contains FileHandler static class
"""


class FileHandler:
    """
    Static class that manages files from reading and writing
    """

    @staticmethod
    def write_line(path, lines):
        """
        The method append a specified line to a specified file path, creates
        the file if the file does not exist in the path.
        :param path: String
        :param lines: String
        """
        if not isinstance(path, str):
            raise TypeError('Invalid file path type!')
        else:
            write_file = open(path, "a+")
            write_file.writelines(f'{lines}\n')
            write_file.close()
