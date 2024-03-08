def write_list_to_file(file_path, input_list):
    try:
        with open(file_path, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"The list has been successfully written to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

output_file_path = r"C:\Users\NEO\Desktop\lab6"
my_list = [1, 2, 3, 4, 5]

write_list_to_file(output_file_path, my_list)
