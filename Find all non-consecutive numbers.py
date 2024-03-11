def all_non_consecutive(arr):
    res = []
    for i, v in enumerate(arr):
        if i == 0:
            continue
        else:
            if v - arr[i-1] != 1:
                res.append({'i': i, 'n': v})
    return res


print(all_non_consecutive([0,1,5,6,8,10,11,12,67]))