import ast
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
    """
    Crypto Class contains two chains of handlers for encryption and decrytion.
    It executes requests from command line to encrypt or decrypt information.
    """

    def __init__(self):
        self.encryption_start_handler = None
        self.decryption_start_handler = None

    def execute_request(self, request: Request):
        if request.encryption_state == CryptoMode.EN:
            self.encryption_start_handler.handle_request(request)
        elif request.encryption_state == CryptoMode.DE:
            self.decryption_start_handler.handle_request(request)


class BaseCryptoHandler(abc.ABC):
    """
    Abstract class that represents behaviour of a crypto handler.
    """
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_handler(self, handler):
        """
        Sets the next handler.
        :param handler: BaseCryptoHandler
        """
        self.next_handler = handler

    def handle_request(self, request: Request):
        pass


class ValidateKeyHandler(BaseCryptoHandler):
    """
    Extends from BaseCryptoHandler class
    Validates key input to check if its length is 8 or 16 or 24.
    """
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
    """
    Extends from BaseCryptoHandler class
    Validates inputs to check if they have valid inputs.
    Inputs can only be either file or command line string.
    Reads a file when valid file input provided.
    """
    def handle_request(self, request: Request):
        print('Validating string input')
        string_input = request.data_input
        file_input = request.input_file
        if string_input and file_input:
            print('cannot have both string input and file input')
            return False
        if string_input and not len(string_input) == 0:
            print('string input found')
            request.input_content = string_input
            if not self.next_handler:
                return True
            return self.next_handler.handle_request(request)
        elif file_input and os.path.exists(file_input):
            print('file input found')
            request.input_content = self.read_file(file_input)
            if not self.next_handler:
                return True
            return self.next_handler.handle_request(request)
        else:
            print('no input found')
            return False

    def read_file(self, file):
        with open(file, 'r') as encrypt_file:
            output = encrypt_file.read()
        return output


class EncryptionHandler(BaseCryptoHandler):
    """
    Extends from BaseCryptoHandler class
    Validates encryption mode from the request and encrypts a message when
    the valid input is provided.
    Default encryption mode is encryotion.
    """
    def handle_request(self, request: Request):
        encryption_state = request.encryption_state
        if encryption_state in (CryptoMode.EN, None):
            print('encrypting')
            request.result = self.encrypt(request.key, request.input_content)
            if not self.next_handler:
                return True
            return self.next_handler.handle_request(request)
        else:
            print('Not encrypt mode')
            return False

    def encrypt(self, key, content):
        byte_key = key.encode('utf-8')
        byte_content = content.encode('utf-8')
        des_key = des.DesKey(byte_key)
        return des_key.encrypt(byte_content, padding=True)


class DecryptionHandler(BaseCryptoHandler):
    """
    Extends from BaseCryptoHandler class
    Validates encryption mode from the request and decrypts a message when
    the valid input is provided.
    """
    def handle_request(self, request: Request):
        encryption_state = request.encryption_state
        if encryption_state == CryptoMode.DE:
            print('Decrypting')
            request.result = self.decrypt(request.key, request.input_content)
            if not self.next_handler:
                return True
            return self.next_handler.handle_request(request)
        else:
            print('Not decrypt mode')
            return False

    def decrypt(self, key, content):
        byte_key = key.encode('utf-8')
        des_key = des.DesKey(byte_key)
        content = ast.literal_eval(content)
        return des_key.decrypt(content, padding=True)


class ValidateOutputHandler(BaseCryptoHandler):
    """
    Extends from BaseCryptoHandler class.
    Validates output methods to check if to print to console or write to file.
    """
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
        with open(file, 'w+') as f:
            f.write(f'{content}\n')


def main(request: Request):
    """
    Main method drives the program.
    Constructs objects of handlers and makes two chains of handler.
    Creates a crypto object and simulates executing requests from commandline
    :param request: Request
    """
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
