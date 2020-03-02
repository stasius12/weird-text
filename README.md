# WeirdText

Simple encryptor and decryptor.

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
