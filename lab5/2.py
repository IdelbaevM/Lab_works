import re

def match_pattern(input_string):
    pattern = re.compile(r'ab{2,3}')
    match = pattern.fullmatch(input_string)
    if match:
        print(f'The string "{input_string}" matches the pattern.')
    else:
        print(f'The string "{input_string}" does not match the pattern.')
test_string = input("Enter a string: ")
match_pattern(test_string)
