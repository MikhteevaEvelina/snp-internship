def count_words(string):
    string = string.lower()
    result = dict()
    s = ''
    for i in string:
        if 'a' <= i <= 'z':
            s += i
        elif s != '':
            if s in result:
                result[s] += 1
            else:
                result[s] = 1
            s = ''
        else:
            continue
    if s != '':
        if s in result:
            result[s] += 1
        else:
            result[s] = 1
    return result


print(count_words('A man, a plan, a canal -- Panama'))
print(count_words('Doo bee doo bee doo'))
