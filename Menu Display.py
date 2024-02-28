"""Create a class that imitates a select screen. The cursor can move to left or right!

In the display method, return a string representation of the list,
but with square brackets around the currently selected element.
Also, create the methods to_the_right and to_the_left which moves the cursor.

The cursor should start at index 0.

Examples
menu = Menu([1, 2, 3])

menu.display() ➞ "[[1], 2, 3]"

menu.to_the_right()
menu.display() ➞ "[1, [2], 3]"

menu.to_the_right()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_right()
menu.display() ➞ "[[1], 2, 3]"

menu.to_the_left()
menu.display() ➞ "[1, 2, [3]]"

menu.to_the_left()
menu.display() ➞ "[1, [2], 3]" """


class Menu:
    def __init__(self, menu=[]):
        self.menu = menu or []
        self.position = 0

    def to_the_right(self):
        if self.position == len(self.menu) - 1:
            self.position = 0
        else:
            self.position += 1

    def to_the_left(self):
        if self.position == 0:
            self.position = len(self.menu) - 1
        else:
            self.position -= 1

    def display(self):
        self.menu = [x for l in self.menu for x in l]
        self.menu[self.position] = list(self.menu[self.position])
        print(str(self.menu))


menu = Menu(['1', '2', '3'])
menu2 = Menu(["a", "b", "c"])
menu2.display()
menu.to_the_left()
menu.display()

menu.to_the_right()
menu.display()

menu.to_the_right()
menu.display()