import sys
import re


def read_each_line_to_list(file):
    result = []
    for line in file:
        arr_str = line.strip().split(',')
        result.append(arr_str)
    file.close()
    return result



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
    print(data)


if __name__ == '__main__':
    main()


