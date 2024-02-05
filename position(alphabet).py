"""When provided with a letter, return its position in the alphabet.
["a", "Position of alphabet: 1"],
["z", "Position of alphabet: 26"],
["e", "Position of alphabet: 5"]"""


def position(alphabet):
    s = "Position of alphabet: " + str(ord(alphabet) - ord('a') + 1)
    return s


