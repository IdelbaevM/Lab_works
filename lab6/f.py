import os

def generate_text_files():
    current_directory = os.getcwd()
    for char_code in range(ord('A'), ord('Z') + 1):
        file_name = chr(char_code) + ".txt"
        file_path = os.path.join(current_directory, file_name)
        
        with open(file_path, 'w') as file:
            file.write(f"This is the content of file {file_name}")

    print("Text files generated successfully.")

generate_text_files()
