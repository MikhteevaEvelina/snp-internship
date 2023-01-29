def coincidence(lst=None, r=None):
    if lst == None or r == None:
        return list()
    all_r = list(r)
    for i in range(len(lst) - 1, -1, -1):
        try:
            item = float(lst[i])
            if item < all_r[0] or item > all_r[-1]:
                lst.pop(i)
        except:
            lst.pop(i)
    return lst


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
