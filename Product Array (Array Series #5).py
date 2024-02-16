"""Given an array/list [] of integers , Construct a product array Of same size
Such That prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].

Array/list size is at least 2 .
Array/list's numbers Will be only Positives
Repetition of numbers in the array/list could occur.
        test.assert_equals(product_array([12,20]), [20,12])
        test.assert_equals(product_array([3,27,4,2]), [216,24,162,324])
        test.assert_equals(product_array([13,10,5,2,9]), [900,1170,2340,5850,1300])
        test.assert_equals(product_array([16,17,4,3,5,2]), [2040,1920,8160,10880,6528,16320])"""


def product_array(l):
    r = 1
    for n in l:
        r *= n
    res = []
    for i in range(len(l)):
        res.append(r // l[i])
    return res
