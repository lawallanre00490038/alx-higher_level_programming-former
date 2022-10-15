#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""
def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""
    for i in range(2):
        for j in range(3):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if (len(matrix[0]) != len(matrix[1])):
        raise TypeError("Each row of the matrix must have the same size")
        
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
        
    if div == 0:
        raise ZeroDivisionError("division by zero")  
    return([[round(i / div, 2) for i in l] for l in matrix])
