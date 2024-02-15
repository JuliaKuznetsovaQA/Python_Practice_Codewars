def find_summands(n):
    s = 0
    for i in range(n):
        s += 2 * i
    x = (n**3 - s) // n
    res = []
    for j in range(n):
        res.append(x + 2 * j)
    return res