"""I've got a crazy mental illness. I dislike numbers a lot. But it's a little complicated:
The number I'm afraid of depends on which day of the week it is...
This is a concrete description of my mental illness:

Monday --> 12
Tuesday --> numbers greater than 95
Wednesday --> 34
Thursday --> 0
Friday --> numbers divisible by 2
Saturday --> 56
Sunday --> 666 or -666
Write a function which takes a string (day of the week) and an integer (number to be tested)
so it tells the doctor if I'm afraid or not. (return a boolean)
sample_test_cases = [
#     day       num  expected
    ('Monday',   13,  False),
    ('Sunday', -666,  True),
    ('Tuesday',   2,  False),
    ('Tuesday', 965,  True),
    ('Friday',    2,  True),"""


def am_I_afraid(day, num):
    if (day == 'Monday' and num == 12) or \
    (day == 'Tuesday' and num > 95) or \
    (day == 'Wednesday' and num == 34) or \
    (day == 'Thursday' and num == 0) or \
    (day == 'Friday' and num % 2 == 0) or \
    (day == 'Saturday' and num == 56) or \
    (day == 'Sunday' and num in (666, -666)):
        return True
    else:
        return False