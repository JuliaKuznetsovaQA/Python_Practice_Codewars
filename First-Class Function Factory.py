"""Write a function, factory, that takes a number as its parameter and returns another function.

The returned function should take an array of numbers as its parameter,
and return an array of those numbers multiplied by the number that was passed into the first function.

In the example below, 5 is the number passed into the first function.
So it returns a function that takes an array and multiplies all elements in it by five.

fives = factory(5)          # returns a function - fives
my_array = [1, 2, 3]
fives(my_array)             # returns [5, 10, 15]"""


def factory(x):
    def my_array(my_arr):
        result = []
        for i in my_arr:
            result.append(i * x)
        return result
    return my_array