# WeirdText

Simple encryptor and decryptor.

## About

### Encoding

For each original word in the original text, leave the first and last character of it in that
position, but shuffle (permutate) all the characters in the middle of the word. If possible,
the resulting “encoded” word MUST NOT be the same as the original word. Keep
everything else (whitespace, punctuation, etc.) like in the original. To make decoding by a
machine possible, your encoder shall also output a sorted list of original words (only
include words that got shuffled, not text that did not).
The composite output of the encoder (see example below) contains encoded text
(WeirdText) and also the sorted list of original words.

### Decoding

For decoding composite text, first do a simple check whether the text looks like composite
output of your encoder. If not, raise some reasonable exception.
Then, use the encoded text and the words list to decode the text.

### Example

Original Text:
‘This is a long looong test sentence, with some big (biiiiig) words!’

Encoded Text:
‘\n—weird—\n'
'Tihs is a lnog loonog tset sntceene, wtih smoe big (biiiiig) wdros!’
‘\n—weird—\n’
‘long looong sentence some test This with words’

Decoded Text:
‘This is a long looong test sentence, with some big (biiiiig) words!’

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.7.5

### Dependencies

* pytest

### Installation guide

First of all clone this repo by typing:

```
git clone https://github.com/stasius12/weird-text
```

Then in created folder create [virtual environment](https://docs.python.org/3/tutorial/venv.html) and run it.
Last step is to install all dependencies:

```
pip install -r requirements.txt
```

To check how the program works we prepare main.py file for you which you can run by:

```
python main.py "The string you want to encode"
```

The result of this function should look like this:

```
Original: The string you want to encode

Encryption:
-weird-
The strnig you wnat to eodnce
-weird-
encode string want

Decryption: The string you want to encode
Verification: True
```

### Tests

To run tests with pytest type in main directory:

```
pytest tests
```

## Authors

* **Stanisław Stępak** - [Connect with me on LinkedIn](https://www.linkedin.com/in/stanislaw-stepak/)
