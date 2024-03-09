give_change1 = lambda x: (x % 5, x % 10 // 5, x % 50 % 20 // 10, x % 50 // 20, x % 100 // 50, x // 100)


def give_change(amount):
    notes = [100, 50, 20, 10, 5, 1]
    array = [0] * len(notes)
    for i, value in enumerate(notes):
        array[i] = amount // value
        amount = amount % value
    array.reverse()
    print(tuple(array))

print(give_change(365)) # (0,1,1,0,1,3))
print(give_change(217)) # (2,1,1,0,0,2))