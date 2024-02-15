"""test.assert_equals(prime_factors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
test.assert_equals(prime_factors(7919), "(7919)")"""


def prime_factors(n):
    res = ''
    i = 2
    while n > 1:
        if n % i != 0:
            i += 1
            continue
        else:
            count = 1
            n = n // i
            while n % i == 0:
                n = n // i
                count += 1
            if count > 1:
                res += f'({i}**{count})'
            elif count == 1:
                res += f'({i})'
            elif count == 0:
                continue
            i += 1
    if res == '':
        res += f'({n})'
    return res


