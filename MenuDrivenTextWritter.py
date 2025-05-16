# function for Writing file
def write_file():
    try:
        filename = input("Enter the filename to write: ")
        content = input("Enter content to write: ")
        with open(filename, 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print("Error: file not found")
    else:
        print("File written successfully.\n")


# function for reading file
def read_file():
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, 'r') as file:
            content = file.read()
            print(f"\nContent of the file {filename} are- \n")
            print(content)
    except FileNotFoundError:
        print("Error: file not found")

# function for appending file
def append_file():
    try:
        filename = input("Enter the filename to append to: ")
        content = input("Enter content to append: ")
        with open(filename, 'a') as file:
            file.write('\n' + content)
        print("Content appended successfully.\n")
    except FileNotFoundError:
        print("Error: file not found")
    else:
        print("File written successfully.\n")


while True:
    print("----- File Operation Menu -----")
    print("1. Write a file")
    print("2. Read a file")
    print("3. Append a file")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        write_file()
    elif choice==2:
        read_file()
    elif choice==3:
        append_file()
    elif choice==4:
        break
    else:
        print("Invalid option. Enter between 1-4")
    
