import pytest
from collections import Counter

from src.encoding import Encryptor
from src.decoding import Decryptor


@pytest.mark.parametrize("text", [
    'This is really big',
    'This, is !!! really ## big **,',
    'This is a long looong test sentence,\nwith some big (biiiiig) words!',
    'Lets say we have a sentence like that one with space at the end ',
    'Lets say we have a sentence like that one!!!!!',
])
def test_decode(text):
    e = Encryptor(text)
    e.encode()
    d = Decryptor(e.result_text)
    d.decode()
    assert d.result_text == text
