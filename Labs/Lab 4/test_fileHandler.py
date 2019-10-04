import os
from unittest import TestCase
from file_handler import FileHandler, InvalidFileTypeError


class TestFileHandler(TestCase):
    def test_load_data_type_error(self):
        self.assertRaises(TypeError, FileHandler.load_data, 123, '')

    def test_load_data_file_not_found_error(self):
        self.assertRaises(FileNotFoundError, FileHandler.load_data,
                          '123.txt', '.txt')

    def test_load_data_invalid_file_type_error(self):
        self.assertRaises(InvalidFileTypeError, FileHandler.load_data,
                          'data.xml', '.xml')

    def test_write_line(self):
        line = 'Hello, testing.'
        os.remove('test.txt')
        FileHandler.write_line('test.txt', line)
        test_file = open('test.txt')
        test_content = test_file.read()
        test_file.close()
        self.assertEqual(test_content, line)
