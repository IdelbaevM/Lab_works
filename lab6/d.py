import os
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

file_path = r"C:\Users\NEO\Desktop\lab6"
lines_count = count_lines(file_path)

if lines_count is not None:
    print(f"The number of lines in the file '{file_path}' is: {lines_count}")
