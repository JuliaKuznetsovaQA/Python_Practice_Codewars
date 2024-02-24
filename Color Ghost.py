"""Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red" """

import random


class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


ghost = Ghost()
print(ghost.color)

ghosts = [Ghost().color for _ in range(100)]
print(ghosts.count("white"))
print(ghosts.count("yellow"))
print(ghosts.count("purple"))
print(ghosts.count("red"))