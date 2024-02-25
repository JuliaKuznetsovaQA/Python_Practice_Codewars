"""This kata is about static method that should return different values.

On the first call it must be 1, on the second and others - it must be a double from previous value."""


class Class:
    cnt = -1

    @staticmethod
    def get_number():
        Class.cnt += 1
        return 2 ** Class.cnt