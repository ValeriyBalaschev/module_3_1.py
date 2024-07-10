# module_3_1.py Домашняя работа по уроку "Пространство имён"


def count_calls():
    global calls
    calls += 1


def string_info(string_):
    count_calls()
    i = ()
    i += len(string_), string_.upper(), string_.lower()
    return i


def is_contains(string_, list_to_search):
    count_calls()
    a = True
    b = ' '.join(list_to_search).lower()
    if b.find(string_.lower()) == -1:
        a = False
    return a


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('Абракадабра'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(is_contains("Клон", ['уклон', "НАКЛОН", "склОН"]))
print(is_contains("Клон", ['слон', "жук", "лёН"]))
print(calls)