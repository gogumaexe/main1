with open('sample.txt', 'w') as f:
    f.write("Hello, this is a sample file.\n")
    f.write("This file contains some test data.")

with open('sample.txt', 'r') as f:
    content = f.read()
    print(content)

def read_whole_file():
    with open('sample.txt', 'r') as file:
        content = file.read()
        print(content)

def read_line_by_line():
    with open('sample.txt', 'r') as file:
        for line in file:
            print(line.strip())

def read_file_into_list():
    with open('sample.txt', 'r') as file:
        lines = file.readlines()
        print(lines)

if __name__ == "__main__":
    read_whole_file()
    
    read_line_by_line()
    
    read_file_into_list()