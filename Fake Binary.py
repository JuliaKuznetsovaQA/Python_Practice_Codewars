"""Given a string of digits, you should replace any digit below 5 with '0' and
any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
            # [expected, input]
            ["01011110001100111", "45385593107843568"],
            ["101000111101101", "509321967506747"],
            ["011011110000101010000011011", "366058562030849490134388085"],
            ["01111100", "15889923"],
            ["100111001111", "800857237867"],"""


def fake_bin(x):
    s = ''
    for i in range(len(x)):
        if int(x[i]) < 5:
            s += '0'
        else:
            s += '1'
    return s