"""Kevin is noticing his space run out! Write a function that removes the spaces from the values and
returns an array showing the space decreasing.
For example, running this function on the array ['i', 'have','no','space']
would produce ['i','ihave','ihaveno','ihavenospace']
test.assert_equals(spacey(['kevin', 'has','no','space']), [ 'kevin', 'kevinhas', 'kevinhasno', 'kevinhasnospace'])
test.assert_equals(spacey(['this','cheese','has','no','holes']), ['this','thischeese','thischeesehas','thischeesehasno','thischeesehasnoholes'])
"""


def spacey(array):
    res = []
    for i, word in enumerate(array):
        res.append(''.join(array[:i+1]))
    return res