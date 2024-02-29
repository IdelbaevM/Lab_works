def split_at_uppercase(input_string):
    result = [input_string[0]]
    for char in input_string[1:]:
        if char.isupper():
            result.append(char)
        else:
            result[-1] += char
    return result
input_string = input("Enter a string: ")
result_list = split_at_uppercase(input_string)
print(f'Split result: {result_list}')
