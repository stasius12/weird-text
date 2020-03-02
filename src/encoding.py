import random
import re

from .base import BaseCryptor


class Encryptor(BaseCryptor):
    """ Encryptr which is taking text as a parameter and
        after executing encode() the result_text attribute contains
        encoded text having the following structure:
        '\n-weird-\n'
        'Here is encoded text'
        '\n-weird-\n'
        'encoded Here text' (this line contains list of words which was encoded - the rest stay the same)
    """
    def __init__(self, text):
        super().__init__(text)
        self.encrypted_words = []

    def _shuffle_word(self, word):
        enc_word = word
        if self._can_word_be_shuffled(word):
            chars_to_shuffle = list(word)[1:-1]
            while enc_word == word:
                random.shuffle(chars_to_shuffle)
                enc_word = word[0] + "".join(chars_to_shuffle) + word[-1]
        return enc_word

    def encode(self):
        for orig_word in self._get_word_generator():
            orig_word = orig_word.group()
            enc_word = self._shuffle_word(orig_word)
            self._refresh_result_text(orig_word, enc_word)
            if enc_word != orig_word:
                self.encrypted_words.append(orig_word)
        self.encrypted_words.sort(key=lambda x: x.lower())
        self.result_text += self.original_text
        self.result_text = (
            self.separator + self.result_text + self.separator + " ".join(self.encrypted_words)
        )
