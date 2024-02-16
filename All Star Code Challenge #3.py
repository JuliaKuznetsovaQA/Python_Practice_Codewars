"""Create a function that takes a string argument and returns that same string with
    all vowels removed (vowels are "a", "e", "i", "o", "u").
"drake" --> "drk"
"aeiou" --> "" """


def remove_vowels(strng):
    s = ''
    for l in strng:
        if l not in 'aeiou':
            s += l
    return s

