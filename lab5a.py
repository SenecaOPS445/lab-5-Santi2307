#!/usr/bin/env python3
# Author ID: sdelgado

def read_file_string(file_name):
    """Reads a file and returns its contents as a single string"""
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    """Reads a file and returns its contents as a list of lines, removing newlines"""
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
