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
    username_arr = [name[2] for name in data]
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
    
    if (sys.argv[1] == '-a'):
        print_unique_name(data)
    elif (sys.argv[1] == '-f'):
        print_number_of_file(data)
        



if __name__ == '__main__':
    main()


