import sys
import re

def read_each_line_to_list(file):
    result = []
    for line in file:
        arr_str = line.strip().split(',')
        result.append(arr_str)
    file.close()
    return result

def print_unique_name(data):
    username_arr = [ele[2] for ele in data]
    unique_arr = []
    for name in username_arr:
        if name not in unique_arr:
            unique_arr.append(name)
    if len(unique_arr) > 0:
        print('Printing users:')
        print(*unique_arr, sep = "\n")
    else:
        print('No printing users')

def print_number_of_file(data):
    print('Total number of files printed:', len(data))

def print_number_of_bytes(data):
    byte_arr = [int(ele[1]) for ele in data]
    print('Total number of bytes printed:', sum(byte_arr))

def print_user_summary(data, username):
    arr = [ele for ele in data if ele[2] == username]
    byte_arr = [int(ele[1]) for ele in arr]
    if len(arr) > 0:
        print(f'User {username}:')
        print('Total number of files printed:', len(arr))
        print('Total number of bytes printed:', sum(byte_arr))
        print('Largest file printed:', max(byte_arr))
    else:
        print(f'User {username} not found')

def main():
    if len(sys.argv) < 3:
        print('Require a file name')
        exit(1)
    else:
        file_name = sys.argv[len(sys.argv) - 1]
        try:
            f = open(file_name, "r")
        except:
            print('Cannot find the file with given name')
            exit(1)
        readable = f.readable()
        if readable == False:
            print('Cannot read the file')
            exit(1)
    
    data = read_each_line_to_list(f)
    
    option = sys.argv[1]

    if (option == '-a'):
        print_unique_name(data)
    elif (option == '-f'):
        print_number_of_file(data)
    elif (option == '-s'):
        print_number_of_bytes(data)
    elif (option == '-u'):
        username = sys.argv[2]
        print_user_summary(data, username)

if __name__ == '__main__':
    main()


