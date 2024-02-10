"""Bob is bored during his physics lessons so he's built himself a toy box to help pass the time.
The box is special because it has the ability to change gravity.
Examples (input -> output:
* 'R', [3, 2, 1, 2]      ->  [1, 2, 2, 3]
* 'L', [1, 4, 5, 3, 5 ]  ->  [5, 5, 4, 3, 1]"""


def flip(d, a):
    if d == "R":
        return sorted(a)
    elif d == "L":
        a.sort()
        a.reverse()
        return a


flip('R', [3, 2, 1, 2])
flip('L', [1, 4, 5, 3, 5])