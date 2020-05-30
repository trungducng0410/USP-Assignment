import sys

def verify_file_input():
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

verify_file_input()
