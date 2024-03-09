lst = [1, 3, 6, 5, 7, 9]
# result = list(map(lambda x: x + 2, lst))
# # print(result)
# print(sum2 := list(map(lambda x: x + 3, lst)))
# print(*sum2, sep='\n')

# a = map(lambda x, y: int(x) * int(y), temp := input().split(), [1, 8, 10, 17, 6])
# print(*a)

# a = list(filter(lambda x: x > 4, lst))
# print(a)

res = lambda x, y: x if x > y else y
print(res(10000, 5))

lst1 = [1, 7, 6, 100, 8, 9]
print(list(filter(lambda x: x % 2, lst1)))

lst2 = ['cat', 'fish', 'dog', 'rabbit']
result = list(filter(lambda x: len(x) > 3, lst2))
print(result)