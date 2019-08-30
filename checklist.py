# -*- coding: utf-8 -*-
import colorama
from colorama import Fore, Back, Style

# Create our Checklist
checklist = []

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
        print('{} {}'.format(index, list_item))
        index += 1

# Adds character to completed item
def mark_completed(index):
    index = '√'
    for list_item in checklist:
        print('{} {}'.format(index,list_item))
        
def select(function_code):
    # Create item
    if function_code == 'A':
        item = user_input(Fore.LIGHTBLUE_EX + 'What do you want to add:  ' + Fore.RESET)
        create(item)

    # Read item
    elif function_code == 'R':
        item_index = user_input(Fore.LIGHTMAGENTA_EX + 'Index Number: ' + Fore.RESET)
        read(int(item_index))
    
    # Destroy item
    elif function_code == 'D':
        index = user_input(Fore.LIGHTGREEN_EX + 'Index Number: ' + Fore.RESET)
        destroy(int(index))

    # Print all items
    elif function_code == 'P':
        for item in checklist:
            print(Fore.LIGHTRED_EX + item + Fore.RESET)
        
    # Mark completed items w/ √
    elif function_code == 'U':
        index = user_input('Index Number: ')
        mark_completed(int(index))

    # Quit program 
    elif function_code == 'Q':
        return False
    
    # Catch all
    else:
        print(Fore.YELLOW + 'Unknown Option' + Fore.RESET)
    return True

#USER INPUT function
def user_input(prompt):
    user_input = input(prompt)
    return user_input

#TEST function
def test():
    #create('purple sox')
    #create('red sox')
    # user_value = user_input("Please enter a value:")
    # print(user_value)

    print(Fore.CYAN + read(0))
    print(read(1))

    update(0,'purple socks')
    destroy(1)

    print(read(0))
    #print(read(1))
    list_all_items()
    mark_completed('√')

    select('C')
    list_all_items()
    select('R')
    list_all_items()

#test()

running = True
while running:
    selection = user_input('Press A to add to list, D to remove from list, U to mark items completed, R to read from the list, P to print list, and Q to quit: ')
    running = select(selection)