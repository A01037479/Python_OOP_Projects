import os

import des
import argparse
import abc
import enum


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """

    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.input_content = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class Crypto:

    def __init__(self):
        self.encryption_start_handler = None
        self.decryption_start_handler = None

    def execute_request(self, request: Request):
        self.encryption_start_handler.handle_request(request)
        self.decryption_start_handler.handle_request(request)


class BaseCryptoHandler(abc.ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_handler(self, handler):
        self.next_handler = handler

    def handle_request(self, request: Request):
        pass


class ValidateKeyHandler(BaseCryptoHandler):
    def handle_request(self, request: Request):
        print('Validating key')
        key_length = len(request.key)
        if key_length in (8, 16, 24):
            print('key is valid')
            if not self.next_handler:
                print('end of chain')
                return True
            return self.next_handler.handle_request(request)
        else:
            print('Key not valid')
            return False


class ValidateInputHandler(BaseCryptoHandler):
    def handle_request(self, request: Request):
        print('Validating string input')
        string_input = request.data_input
        file_input = request.input_file
        if string_input:
            print('string input found')
            request.input_content = string_input
            if not self.next_handler:
                print('end of chain')
                return True
            return self.next_handler.handle_request(request)
        elif file_input and os.path.exists(file_input):
            print('file input found')
            request.input_content = self.read_file(file_input)
            if not self.next_handler:
                print('end of chain')
                return True
            return self.next_handler.handle_request(request)
        else:
            print('no input found')
            return False

    def read_file(self, file):
        with open(file, 'r') as f:
            output = f.read()
        return output


# class StringInputHandler(BaseCryptoHandler):
#     def handle_request(self, request: Request):
#         print('Validating string input')
#         string_input = request.data_input
#         if string_input:
#             print('string input found')
#             request.input_content = string_input
#             if not self.next_handler:
#                 print('end of chain')
#                 return True
#         else:
#             print('string input is empty')
#         return self.next_handler.handle_request(request)
#
#
# class FileInputHandler(BaseCryptoHandler):
#     def handle_request(self, request: Request):
#         print('Validating file input')
#         file_input = request.input_file
#         if file_input is not None and os.path.exists(file_input):
#             print('file input found')
#             request.input_content = self.read_file(file_input)
#             if not self.next_handler:
#                 print('end of chain')
#                 return True
#         else:
#             print('input is not specified '
#                   'or file input not valid')
#         return self.next_handler.handle_request(request)
#
#     def read_file(self, file):
#         with open(file, 'r') as f:
#             output = f.read()
#         return output


class EncryptionHandler(BaseCryptoHandler):
    def handle_request(self, request: Request):
        encryption_state = request.encryption_state
        if encryption_state in (CryptoMode.EN, None):
            print('encrypting')
            request.result = self.encrypt(request.input_content)
            if not self.next_handler:
                return True
            return self.next_handler.handle_request(request)
        else:
            print('Not encrypt mode')
            return False

    def encrypt(self, content):
        result = content
        return result


class DecryptionHandler(BaseCryptoHandler):
    def handle_request(self, request: Request):
        encryption_state = request.encryption_state
        if encryption_state == CryptoMode.DE:
            print('Decrypting')
            request.result = self.decrypt(request.input_content)
            if not self.next_handler:
                return True
            return self.next_handler.handle_request(request)
        else:
            print('Not decrypt mode')
            return False

    def decrypt(self, content):
        result = content
        return result


class ValidateOutputHandler(BaseCryptoHandler):
    def handle_request(self, request: Request):
        print('validating output type')
        if request.output in ('print', None):
            print('printing result to console')
            print(f'result: {request.result}')
            if not self.next_handler:
                return True
            return self.next_handler.handle_request(request)
        elif request.output.lower().endswith('.txt'):
            print(f'writing file to file {request.output}')
            self.write_file(request.result, request.output)
            if not self.next_handler:
                return True
            return self.next_handler.handle_request(request)
        else:
            print('invalid output file path')

    def write_file(self, content, file):
        with open(file, 'a+') as f:
            f.write(f'{content}\n')


class PrintToConsoleHandler(BaseCryptoHandler):
    def handle_request(self, request: Request):
        print('validating if printing result to console')
        if request.output in ('print', None):
            print('printing result to console')
            print(f'result: {request.result}')
            if not self.next_handler:
                return True
        else:
            print('not printing to console')
        return self.next_handler.handle_request(request)


class WriteToFileHandler(BaseCryptoHandler):
    def handle_request(self, request: Request):
        print('validating if writing result to file')
        if request.output.lower().endswith('.txt'):
            print(f'writing file to file {request.output}')
            self.write_file(request.result, request.output)
            if not self.next_handler:
                return True
        else:
            print('not writing file')
        return self.next_handler.handle_request(request)

    def write_file(self, content, file):
        with open(file, 'r') as f:
            f.write(content)


def main(request: Request):
    crypto = Crypto()
    vkh_e = ValidateKeyHandler()
    vih_e = ValidateInputHandler()
    eh_e = EncryptionHandler()
    voh_e = ValidateOutputHandler()
    vkh_e.set_handler(vih_e)
    vih_e.set_handler(eh_e)
    eh_e.set_handler(voh_e)

    vkh_d = ValidateKeyHandler()
    vih_d = ValidateInputHandler()
    dh_d = DecryptionHandler()
    voh_d = ValidateOutputHandler()
    vkh_d.set_handler(vih_d)
    vih_d.set_handler(dh_d)
    dh_d.set_handler(voh_d)

    crypto.encryption_start_handler = vkh_e
    crypto.decryption_start_handler = vkh_d
    crypto.execute_request(request)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
