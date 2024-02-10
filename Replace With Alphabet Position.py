"""In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc."""


def alphabet_position(text):
    s = ''
    for i in text.lower():
        if i.isalpha():
            s += str(ord(i) - 96) + ' '
        else:
            continue
    return s.strip()


# в одну строку:

def alphabet_position_(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())