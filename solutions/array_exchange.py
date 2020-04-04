def rev_copy_list(l1, l2):
    l1.clear()
    l2.reverse()
    for i, val in enumerate(l2):
        l1.append(val)


def exchange_with(a, b):
    temp = a.copy()
    rev_copy_list(a, b)
    rev_copy_list(b, temp)


if __name__ == '__main__':
    a = ["1", "2", "3", "4", "5", "6", "7"]
    b = ["a", "b", "c"]
    exchange_with(a, b)
    assert a == ["c", "b", "a"]
    assert b == ["7", "6", "5", "4", "3", "2", "1"]
