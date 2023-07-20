def factorial(number: int):
    if number == 1:
        return number
    return number *factorial(number - 1)

print(factorial(5))

import os

current_path = os.path.abspath(__file__)
parent_path =os.path.join(current_path, '..')
parent_path_parent = os.path.join(parent_path, '..')
print(parent_path)

new_file =open()

def get_all_paths(path):
    for i_file in os.listdir(path):
        new_path =os.path.join(path, i_file)
        if os.path.isdir(new_path):
            print(new_path)
            get_all_paths(new_path)
        else:
            print('\t-',new_path)
get_all_paths(parent_path_parent)




