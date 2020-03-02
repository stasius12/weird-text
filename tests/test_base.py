import pytest

from src.base import BaseCryptor


@pytest.mark.parametrize("word,expected_return", [
    ('b', False),
    ('big', False),
    ('biiig', False),
    ('home', True),
    ('aloha', True)
])
def test_can_word_be_shuffled(word, expected_return):
    b = BaseCryptor('')
    assert b._can_word_be_shuffled(word) == expected_return


@pytest.mark.parametrize("text,words", [
    ('This is really big', ['This', 'is', 'really', 'big']),
    ('This, is !!! really ## big **,', ['This', 'is', 'really', 'big']),
])
def test_word_generator(text, words):
    b = BaseCryptor(text)
    it = b._get_word_generator()
    assert [x.group() for x in it] == words


@pytest.mark.parametrize("text,orig_word,enc_word,result", [
    (
        'This is really big', 'This', 'Tihs', 'Tihs '
    )
])
def test_refresh_result_text(text, orig_word, enc_word, result):
    b = BaseCryptor(text)
    b._refresh_result_text(orig_word, enc_word)
    assert b.result_text == result
