"""You will be given an array that contains two strings.
Your job is to create a function that will take those two strings and transpose them,
so that the strings go from top to bottom instead of left to right.

e.g. transposeTwoStrings(['Hello','World']);  should return

H W
e o
l r
l l
o d
A few things to note:
There should be one space in between the two characters
You don't have to modify the case (i.e. no need to change to upper or lower)
If one string is longer than the other, there should be a space where the character would be
        test.assert_equals(transpose_two_strings(["Hello","World"]), "H W\ne o\nl r\nl l\no d")
        test.assert_equals(transpose_two_strings(["joey","louise"]), "j l\no o\ne u\ny i\n  s\n  e")
        test.assert_equals(transpose_two_strings(["a","cat"]), "a c\n  a\n  t")
        test.assert_equals(transpose_two_strings(["cat",""]), "c  \na  \nt  ")
        test.assert_equals(transpose_two_strings(["!a!a!","?b?b"]), "! ?\na b\n! ?\na b\n!  ") """


def transpose_two_strings(arr):
    lenth = max(len(arr[0]), len(arr[1]))
    arr[0] = arr[0].ljust(lenth)
    arr[1] = arr[1].ljust(lenth)
    res = [list(arr[0]), list(arr[1])]
    s = ''
    for i in range(lenth):
        s += res[0][i] + ' ' + res[1][i] + '\n'
    return s[:-1]