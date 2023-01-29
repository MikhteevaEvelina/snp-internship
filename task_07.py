def combine_anagrams(words_array):
    group_words = dict()
    answer = []
    for w in words_array:
        lst = list(w)
        lst.sort()
        anagram = ''.join(lst)
        if anagram in group_words:
            group_words[anagram].append(w)
        else:
            group_words[anagram] = [w]
    for val in group_words.values():
        answer.append(val)
    return answer


print(combine_anagrams(['cars', 'for', 'potatoes',
                        'racs', 'four', 'scar', 'creams', 'scream']))
