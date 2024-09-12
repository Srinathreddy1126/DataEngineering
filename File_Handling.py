import os
filename1 = "C:\\Users\\srinathreddy\\Documents\\File Reading\\Doc.txt"
k='Hello world !!!'

def read_file(filename=filename1):
    try:
        with open(filename,'r') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print('File does not exist and is created now')
        with open(filename, 'w') as f:
            f.write(k + filename1)
            print("File " + filename + " created successfully.")


def create_file(text,filename=filename1):
    try:
        kp = text + 'Hello, world'
        with open(filename, 'w') as f:
            f.write(kp)
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)


def append_file(text,filename=filename1):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)


print('Choose the file operation no you want to perform')
print('1.Read a File  2.Create a File  3.Append a File')
num = int(input())

match num:

    case 1:
        print('Enter file name and path')
        inp = input()
        read_file(inp)

    case 2:
        print('A file will be created, enter some text')
        inp= input()
        create_file(inp, filename1)

    case 3:
        print('Enter the file name and text to be appended')
        inp = input()
        append_file(inp)

