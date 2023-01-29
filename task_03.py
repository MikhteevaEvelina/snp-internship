def max_odd(array):
    odd_arr = []
    for item in array:
        try:
            i = float(item)
            if (i == int(i)) and (i % 2 != 0):
                odd_arr.append(int(i))
        except:
            continue
    if len(odd_arr) == 0:
        return None
    else:
        return max(odd_arr)


print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))
