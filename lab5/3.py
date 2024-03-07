import re

def find_sequences(input_string):
    pattern = re.compile(r'[a-z]+_[a-z]+')
    matches = pattern.findall(input_string)
    if matches:
        print(f'Sequences found: {matches}')
    else:
        print('No sequences found.')
test_string = input("Enter a string: ")
find_sequences(test_string)