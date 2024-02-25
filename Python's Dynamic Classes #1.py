class MyClass:
    pass


def class_name_changer(cls, new_name):
    if new_name.isalnum() and new_name[0].isupper() and new_name[0].isalpha() and len(new_name) > 0:
        cls.__name__ = new_name
    else:
        raise Exception('Error!')


class_name_changer(MyClass, 'NewClass')
print(MyClass.__name__)