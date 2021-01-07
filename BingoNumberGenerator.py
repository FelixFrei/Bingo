import os
import numpy as np
import random as rand

file_path = 'numbers.csv'
min_number = 1
max_number = 90

# open or create the file
mode = 'a' if os.path.exists(file_path) else 'w'
file = open(file_path, mode)

# generate empty array
all_numbers = np.empty(shape=[0])

# read csv file and put the numbers into arry
if os.fstat(file.fileno()).st_size:
    all_numbers = np.loadtxt(file_path, delimiter=',')

random_number = rand.randint(min_number, max_number)


if np.size(all_numbers) < max_number:
    if np.size(all_numbers) > 0:
        while(random_number in (all_numbers)):
            random_number = rand.randint(min_number, max_number)
    print("------------------")
    print("------- " + str(random_number) + " -------")
    print("------------------")
    all_numbers = np.append(all_numbers, random_number)
    # save array as integer to csv file
    np.savetxt(file_path, all_numbers, fmt='%i', delimiter=',')
else:
    print("Fertig! Nummern komplett!!")







