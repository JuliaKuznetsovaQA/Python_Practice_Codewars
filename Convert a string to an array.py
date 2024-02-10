"""Write a function to split a string and convert it into an array of words.
test.assert_equals(string_to_array("Robin Singh"), ["Robin", "Singh"])
test.assert_equals(string_to_array("CodeWars"), ["CodeWars"])
test.assert_equals(string_to_array("I love arrays they are my favorite"),
                   ["I", "love", "arrays", "they", "are", "my", "favorite"])
test.assert_equals(string_to_array("1 2 3"), ["1", "2", "3"])"""


def string_to_array(s):
    if s == "":
        return ['']
    else:
        return s.split()