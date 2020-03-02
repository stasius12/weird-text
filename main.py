import sys

from src.encoding import Encryptor
from src.decoding import Decryptor


def run(text):
    e = Encryptor(text)
    e.encode()

    d = Decryptor(e.result_text)
    d.decode()
    return e.result_text, d.result_text


if __name__ == '__main__':
    text = sys.argv[1]
    print(f'\nOriginal: {text}\n')
    encryption, result = run(text)
    print(f'Encryption: {encryption}\n\nDecryption: {result}\nVerification: {text == result}')
