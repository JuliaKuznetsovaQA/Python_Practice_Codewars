"""A Tidy number is a number whose digits are in non-decreasing order.
Given a number, Find if it is Tidy or not .
Number passed is always Positive .
Return the result as a Boolean

        test.assert_equals(tidyNumber(12), True)
        test.assert_equals(tidyNumber(102), False)
        test.assert_equals(tidyNumber(9672), False)
        test.assert_equals(tidyNumber(2789), True)"""


def tidyNumber(n):
    x = 0
    flag = True
    for i in str(n):
        if int(i) < x:
            flag = False
        x = int(i)
    return flag