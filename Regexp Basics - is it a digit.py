import re


def is_digit(n):
    print(bool(re.fullmatch(r'\d', n)))


is_digit(" ")