with open('sample.txt', 'a') as f:
    f.write("\nAppending new content to the file.")

def write_to_file():
    with open('sample.txt', 'w') as file:
        file.write("привет\n")
        file.write("это пример\n")

def append_to_file():
    with open('sample.txt', 'a') as file:
        file.write("новая строка\n")

if __name__ == "__main__":
    print("запись")
    write_to_file()

    print("\nдобавить")
    append_to_file()