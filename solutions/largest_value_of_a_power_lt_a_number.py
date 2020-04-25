def largest_power(n):
    if n == 1: return 0, -1
    if 1 < n < 5: return 1, -1
    max_v, count, a, b = 0, 0, 2, 2
    res = a ** b
    while res < n:
        while res < n:
            if res == max_v:
                count += 1
            elif res > max_v:
                max_v, count = res, 1
            a += 1
            res = a ** b
        a, b = 2, b + 1
        res = a ** b
    return max_v, count


if __name__ == '__main__':
    assert largest_power(90) == (81, 2)
    assert largest_power(6) == (4, 1)
    assert largest_power(3) == (1, -1)
    assert largest_power(1) == (0, -1)
    assert largest_power(81) == (64, 3)
    assert largest_power(4) == (1, -1)
