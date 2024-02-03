def greet(name):
    if name == "Johnny":
        print("Hello, my love!")
    else:
        print("Hello, {}!".format(name))

username = input()
greet(username)