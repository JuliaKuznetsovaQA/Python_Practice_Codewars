"""Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).
The next words should be always capitalized.
Examples:
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"The_Stealth-Warrior" gets converted to "TheStealthWarrior" """


def to_camel_case(text):
    if text == '':
        return ''
    else:
        l = text.split('_')
        n = ' '.join(l)
        v = n.split('-')
        second = ' '.join(v)
        if second[0].isupper():
            third = second.split()
            forth = []
            for word in third:
                forth.append(word.title())
        else:
            third = second.split()
            forth = [third[0]]
            for i in range(1, len(third)):
                forth.append(third[i].title())
        return ''.join(forth)