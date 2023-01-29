def connect_dicts(dict1, dict2):
    sum1 = 0
    sum2 = 0
    result = dict()
    for val in dict1.values():
        sum1 += val
    for val in dict2.values():
        sum2 += val
    if sum1 > sum2:
        first = dict1
        second = dict2
    else:
        first = dict2
        second = dict1
    for key in first:
        if first[key] >= 10:
            result[key] = first[key]
        else:
            continue
    for key in second:
        if second[key] >= 10 and key not in result:
            result[key] = second[key]
        else:
            continue
    return (dict(sorted(result.items(), key=lambda x: x[1])))


print(connect_dicts({'a': 2, 'b': 12}, {'c': 11, 'e': 5}))
print(connect_dicts({'a': 13, 'b': 9, 'd': 11}, {'c': 12, 'a': 15}))
print(connect_dicts({'a': 14, 'b': 12}, {'c': 11, 'a': 15}))
