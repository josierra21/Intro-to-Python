#DSC510
#Week9: File Operations, Error Handling
#Programming Assignment Week9
#Author Joanna Sierra-Mendoza
#02/05/24

import string
import sys

def process_line(line, word_count):
    words = line.split()
    for word in words:
        word = word.lower()
        word = word.strip(string.punctuation)
        add_word(word, word_count)



def add_word(word, word_count):
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1


def pretty_print(word_count):
    value_key_list=[]
    for key, val in word_count.items():
        value_key_list.append((val,key))
    value_key_list.sort(reverse=True)
    print('{:11s}{:11s}'.format("Word", "Count"))
    print('_________________')
    print(' '*21)
    for val, key in value_key_list:
        print('{:12s} {:<3d}'.format(key,val))


def process_file(word_count):
    fname = input('ENTER THE FILE NAME:')
    f = open(fname, "w")
    sys.stdout = f
    value_key_list = []
    for key, val in word_count.items():
        value_key_list.append((val, key))
    value_key_list.sort(reverse=True)
    print('{:11s}{:11s}'.format("Word", "Count"))
    print('_________________')
    print(' ' * 21)
    for val, key in value_key_list:
        print('{:12s} {:<3d}'.format(key, val))


def main():
    word_count = {}
    file_name = 'gettysburg.txt'
    try:
        with open('gettysburg.txt', 'r') as fhand:
            for line in fhand:
                process_line(line, word_count)
            pretty_print(word_count)
        process_file(word_count)
        print('Length of the Dictionary:', len(word_count))
    except FileNotFoundError:
        print("File was not located")


if __name__ == "__main__":
    main()
