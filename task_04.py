def sort_list(list):
    if (len(list) == 0):
        return(list)
    elif (len(list) == 1):
        list.append(list[0])
        return list
    min = list[0]
    max = list[0]
    for i in range(1, len(list)):
        if list[i] < min:
            min = list[i]
        elif list[i] > max:
            max = list[i]
    for i in range(len(list)):
        if list[i] == min:
            list[i] = max
        elif list[i] == max:
            list[i] = min
    list.append(min)
    return list


print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))
