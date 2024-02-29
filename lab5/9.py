def insert_spaces(input_string):
    result = [input_string[0]]
    for char in input_string[1:]:
        if char.isupper():
            result.append(' ')
        result.append(char)
    
    return ''.join(result)
input_string = input("Enter a string: ")
result_string = insert_spaces(input_string)
print(f'Result string: {result_string}')
