"""
This modules contains a test case class for file handler class
"""
import os
from unittest import TestCase
from file_handler import FileHandler, InvalidFileTypeError


class TestFileHandler(TestCase):
    """
    The class contains unit testing for File Handler class
    """
    def test_load_data_type_error(self):
        """
        Tests the method load_data from FileHandler.
        Checks if TypeError is raised when an integer type file path is entered.
        """
        self.assertRaises(TypeError, FileHandler.load_data, 123, '')

    def test_load_data_file_not_found_error(self):
        """
        Tests the method load_data from FileHandler.
        Checks if FileNotFoundError is raised when the specified file path does
        not exist.
        """
        self.assertRaises(FileNotFoundError, FileHandler.load_data,
                          '123.txt', '.txt')

    def test_load_data_invalid_file_type_error(self):
        """
        Tests the method load_data from FileHandler.
        Checks if InvalidFileTypeError is raised when an incorrect format of
        file extension is entered.
        """
        self.assertRaises(InvalidFileTypeError, FileHandler.load_data,
                          'data.xml', '.xml')

    def test_write_line(self):
        """
        Tests the method write_line from FileHandler.
        Checks if the specified line is written in a specified file path.
        """
        line = 'Hello, testing.'
        os.remove('test.txt')
        FileHandler.write_line('test.txt', line)
        test_file = open('test.txt')
        test_content = test_file.read()
        test_file.close()
        self.assertEqual(test_content, line)
