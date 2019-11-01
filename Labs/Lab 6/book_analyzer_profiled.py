"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = [",", "*", ";", ".", ":", "(", "[", "]", ")"]

    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        translator = str.maketrans("", "", "".join(self.COMMON_PUNCTUATION))
        with open(src, mode='r', encoding='utf-8') as book_file:
            words = book_file.read().split()
            self.text = [word.translate(translator) for word in words]

    @staticmethod
    def is_unique(word, word_list):
        """
        Checks to see if the given word appears in the provided sequence.
        This check is case in-sensitive.
        :param word: a string
        :param word_list: a sequence of words
        :return: True if not found, false otherwise
        """
        for a_word in word_list:
            if word == a_word:
                return False
        return True

    def find_unique_words(self):
        """
        Filters out all the words that only appear once in the text.
        :return: a list of all the unique words.
        """
        temp_text = [word.lower() for word in self.text]
        unique_words = []
        duplicate_words = []
        while temp_text:
            word = temp_text.pop()
            if word not in duplicate_words:
                if self.is_unique(word, temp_text):
                    unique_words.append(word)
                else:
                    duplicate_words.append(word)
        return unique_words


def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    unique_words = book_analyzer.find_unique_words()
    print("-" * 50)
    print(f"List of unique words (Count: {len(unique_words)})")
    print("-" * 50)
    for word in unique_words:
        print(word)
    print("-" * 50)


if __name__ == '__main__':
    main()
