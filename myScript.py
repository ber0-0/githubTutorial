import numpy as np
import pandas as pd

def my_func(matrix_1, matrix_2):
    try:
        return matrix_1 * matrix_2
    except ValueError:
        print("Matrix size is not aligned!")
        return None

#n = input("Enter an integer:")

#for i in range(n):
#    print(n)

my_matrix = np.identity(5)
second_matrix = np.random.random(size=(5,4))

print(my_matrix, second_matrix)
