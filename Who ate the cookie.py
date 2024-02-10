"""For this problem you must create a program that says who ate the last cookie.
If the input is a string then "Zach" ate the cookie.
If the input is a float or an int then "Monica" ate the cookie.
If the input is anything else "the dog" ate the cookie.
The way to return the statement is: "Who ate the last cookie? It was (name)!"

Ex: Input = "hi" --> Output = "Who ate the last cookie? It was Zach!
(The reason you return Zach is because the input is a string)
"""


def cookie(x):
    if type(x) == str:
        name = 'Zach'
    elif type(x) == float or type(x) == int:
        name = 'Monica'
    else:
        name = 'the dog'
    return f'Who ate the last cookie? It was {name}!'

