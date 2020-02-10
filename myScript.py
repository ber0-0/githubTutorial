import numpy as np
import pandas as pd

def my_func(matrix_1, matrix_2):
    return matrix_1 * matrix_2

my_matrix = np.identity(4)
second_matrix = np.identity(4)

print(my_func(my_matrix, second_matrix))


#n = input("Enter an integer:")

#for i in range(n):
#    print(n)


#print(my_matrix)