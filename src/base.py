import random
import re


class BaseCryptor:
    """
    Base Class for both encryption and decryption
    """
    def __init__(self, text):
        self.original_text = text
        self.result_text = ''
        self.separator = '\n-weird-\n'

    def _can_word_be_shuffled(self, word):
        return True if len(word) > 3 and len(set(word[1:-1])) > 1 else False

    def _get_word_generator(self):
        pattern = re.compile(r'(\w+)', re.A)
        return pattern.finditer(self.original_text)

    def _refresh_result_text(self, orig_word, enc_word):
        idx = self.original_text.index(orig_word) + len(orig_word) + 1
        enc_text = self.original_text[:idx].replace(
            orig_word, enc_word
        )
        self.result_text += enc_text
        self.original_text = self.original_text[idx:]
