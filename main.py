calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    string = f'{len(string), string.upper(),string.lower()}'
    return f'{string} {count_calls()}'

def is_contains(string, list_to_search):
    if any(item in string for item in list_to_search):
        return f'{True} {count_calls()}'
    else:
        return f'{False} {count_calls()}'


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)