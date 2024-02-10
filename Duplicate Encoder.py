"""The goal of this exercise is to convert a string to a new string where each character
in the new string is "(" if that character appears only once in the original string,
or ")" if that character appears more than once in the original string.
Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("  """


def duplicate_encode(word):
    n = set()
    y = set()
    w = word.lower()
    res = ''
    for i in w:
        if i in n:
            y.add(i)
        else:
            n.add(i)
    for i in w:
        if i in y:
            res += ')'
        else:
            res += '('
    return res