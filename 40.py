string=input('Введите строку строчными буквами без пробелов.')
def palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string
print(palindrome(string))
