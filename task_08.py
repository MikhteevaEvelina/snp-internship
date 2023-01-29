def multiply_numbers(inputs=None):
    result = None
    if inputs == None:
        return result
    if type(inputs) == set:
        s = ''.join(inputs)
    else:
        s = str(inputs)
    for i in s:
        if '0' <= i <= '9':
            if result == None:
                result = int(i)
            else:
                result *= int(i)
        else:
            continue
    return result


print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))
