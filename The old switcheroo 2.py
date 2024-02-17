"""Write the function that takes in a string str and replaces all the letters
with their respective positions in the English alphabet.

encode('abc') == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
encode('codewars') == '315452311819'
encode('abc-#@5') == '123-#@5'"""


def encode(string):
    s = ''
    for i in string:
        if i.isalpha():
            s += str(ord(i.lower()) - 96)
        else:
            s += i
    return s

