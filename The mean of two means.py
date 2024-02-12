"""Write a function that takes as parameters an array (arr) and 2 integers (x and y).
The function should return the mean between the mean of the the first x elements of the array
and the mean of the last y elements of the array.

The mean should be computed if both x and y have values higher than 1 but less or equal to the array's length.
Otherwise the function should return -1.
        test.assert_equals(get_mean([1,3,2,4],2,3),2.5)
        test.assert_equals(get_mean([1,3,2],2,2),2.25)
        test.assert_equals(get_mean([1,3,2,4],1,2),-1)
        test.assert_equals(get_mean([1,3,2,4],2,8),-1)
        test.assert_equals(get_mean([1,-1,2,-1],2,3),0)"""


def get_mean(arr, x, y):
    if x <= 1 or y <= 1 or x > len(arr) or y > len(arr):
        return -1
    else:
        total1 = 0
        total2 = 0
        for i in range(x):
            total1 += arr[i]
        for i in range(len(arr) - y, len(arr)):
            total2 += arr[i]
        if (total1 / x + total2 / y) == 0:
            return 0
        else:
            return (total1 / x + total2 / y) / 2


# красивое решение:

def get_mean(arr,x,y):
    if 1 < x <= len(arr) and 1 < y <= len(arr):
       return (sum(arr[:x])/x+sum(arr[-y:])/y)/2
    return -1