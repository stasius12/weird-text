from collections import Counter

from .base import BaseCryptor
from .exceptions import SeparatorMismatchException, NoMatchFoundException


class Decryptor(BaseCryptor):
    """ Decryptor which is taking encrypted text as a parameter and
        after executing decode() the result_text attribute contains decoded text.
    """
    def __init__(self, text):
        super().__init__(text)
        self.result_words = []
        self._separate_weird_text_from_words()

    def _separate_weird_text_from_words(self):
        left, sep, right = self.original_text.rpartition(self.separator)
        if sep != self.separator:
            raise SeparatorMismatchException
        self.original_text = left.replace(self.separator, '')
        self.result_words = right.strip().split(' ')

    def _find_best_match_for_word(self, enc_word):
        if not self._can_word_be_shuffled(enc_word):
            return enc_word
        try:
            return next(
                r_word for r_word in self.result_words
                if Counter(r_word) == Counter(enc_word) and r_word[0] == enc_word[0] and r_word[-1] == enc_word[-1]
            )
        except StopIteration:
            raise NoMatchFoundException

    def decode(self):
        for word in self._get_word_generator():
            word = word.group()
            match = self._find_best_match_for_word(word)
            if match is not None:
                self._refresh_result_text(word, match)
        self.result_text += self.original_text
