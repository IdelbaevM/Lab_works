def camel_to_snake(camel_case_string):
    result = [camel_case_string[0].lower()]
    for char in camel_case_string[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)
    
    return ''.join(result)
camel_case_input = input("Enter a camel case string: ")
snake_case_output = camel_to_snake(camel_case_input)
print(f'Snake case string: {snake_case_output}')
