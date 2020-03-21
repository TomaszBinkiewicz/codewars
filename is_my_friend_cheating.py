def removNb(n):
    input_values = [i for i in range(n + 1)]
    total_sum = sum(input_values)
    ret_list = []
    for i in input_values:
        float_j = (total_sum - i) / (i + 1)
        j = int(float_j)
        if j == float_j and j in input_values and i != j:
            ret_list.append((i, j))
    return ret_list


if __name__ == '__main__':
    assert removNb(100) == []
    assert removNb(26) == [(15, 21), (21, 15)]
