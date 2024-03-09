# f= lambda a,b,n=0: (a,(a+b)//2, n+1) while a!=b:

def f(a, b):
    c = 0
    while a != b:
        b = (a + b) // 2
        c += 1
    return c


print(f(0, 0)) # 0, 'Input a=0, b=0')
print(f(1, 2)) # 1, 'Input a=1, b=2')
print(f(3, 9)) # 3, 'Input a=3, b=9')
print(f(4, 20)) # 5, 'Input a=4, b=20')
print(f(5, 36)) # 5, 'Input a=5, b=36')