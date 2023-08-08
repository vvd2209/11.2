def capital_letters(words):
    """
    функция, которая принимает на вход строку и возвращает ее со всеми заглавными буквами.
    """
    string_words = words.upper()
    return string_words

string_words = input()
result = capital_letters(string_words)
print(result)
