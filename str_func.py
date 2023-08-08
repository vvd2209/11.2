def capital_letters(words):
    """
    Функция, которая принимает на вход строку и возвращает ее со всеми заглавными буквами
    """
    string_words = words.upper()
    return string_words

string_words = input()
result = capital_letters(string_words)
print(result)

def capital_first_letters(words):
    """
    Функция, которая принимает на вход строку и
    возвращает ее с заглавными первыми буквами каждого слова
    """
    string_words = words.title()
    return string_words

string_words = input()
result = capital_first_letters(string_words)
print(result)