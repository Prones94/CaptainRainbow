# -*- coding: utf-8 -*-

from colorama import Fore, Back, Style # prints colors to terminal output

# Create our Checklist
checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index,item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)
    
# LIST
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# Adds character to completed item
def mark_completed(index):
    index = '√'
    for list_item in checklist:
        print("{}{}".format(index,list_item))
        


#TEST function
def test():
    create('purple sox')
    create('red sox')

    print(Back.MAGENTA + Fore.BLACK + read(0))
    print(Back.RED + read(1))

    update(0,'purple socks')
    destroy(1)

    print(Back.MAGENTA + read(0))
    #print(read(1))
    list_all_items()
    mark_completed('√')

test()
