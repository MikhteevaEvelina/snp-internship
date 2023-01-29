def is_palindrome(string):
    string = str(string)
    symbols = []
    for let in string:
        if 'A' <= let <= 'Z' or 'a' <= let <= 'z' or '0' <= let <= '9':
            symbols.append(let.upper())
    for i in range(len(symbols) // 2 + 1):
        if symbols[i] != symbols[len(symbols) - 1 - i]:
            return False
    return True


print(is_palindrome('A man, a plan, a canal -- Panama'))
print(is_palindrome("Madam, I'm Adam"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome('Abracadabra'))
