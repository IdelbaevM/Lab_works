import re

def m_p(input_string):
    pattern = re.compile(r'a*b*')
    match = pattern.fullmatch(input_string)
    if match:
        print(f'The string "{input_string}" matches the pattern.')
    else:
        print(f'The string "{input_string}" does not match the pattern.')
test_string = input("Enter a string: ")
m_p(test_string)
