#!/usr/bin/env python3
# Author ID: cthomas49

def read_file_string(file_name):
     # Takes file_name as string for a file name, returns its entire contents as a string
     f = open(file_name, 'r')
     file_contents = f.read()
     f.close()
     return file_contents

def read_file_list(file_name):
    # Takes a file_name as string for a file name, return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    list_of_lines_with_newlines = list(f)
    
    list_of_lines = []
    for line in list_of_lines_with_newlines:
        list_of_lines.append(line.strip())
    
    f.close()
    return list_of_lines
    

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
