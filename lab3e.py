#!/usr/bin/env python3
'''Lab 3 Inv 3 functions with lists '''
# Author ID: ajjayaratnam

# Global list
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Return all items in the list unchanged
    return my_list

def give_first_item():
    # Return the first item in the list as a string
    return str(my_list[0])

def give_first_and_last_item():
    # Return a list containing the first and last items
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Return a list containing the second and third items
    return [my_list[1], my_list[2]]

if __name__ == '__main__':
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())
