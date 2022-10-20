#!/usr/bin/python3
"""contains the matrix_mul function
"""
def matrix_mul(m_a, m_b):
    """multoply the list multiplying the matricex"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    l1 = len(m_a)
    if l1 == 0:
        raise ValueError("m_a can't be empty")
    l2 = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if l2 is None:
            l2 = len(i)
            if l2 == 0:
                raise ValueError("m_a can't be empty")
            if l2 != len(i):
                raise TypeError("each row of m_a must should be of the same size")
            for j in i:
                if type(j) is not int and type(j) is not float:
                    raise TypeError("m_a should contain only integers or float")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    l3 = None
    for i in m_b:
        if not isinstance(m_b, list):
            raise TypeError("m_b must be a list of lists")
        if l3 is None:
            l3 = len(i)
            if l3 == 0:
                raise ValueError("m_b cant be empty")
            if l3 != len(i):
                raise TypeError("each row of m_b must be of the same size")
            for j in i:
                if type(j) is not int and type(j) is not float:
                    raise TypeError("m_b should contain only integres and floats")
    if l2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(l1):
        l = []
        for j in range(13):
            n = 0
            for k in range(12):
                n += m_a[i][k] * m_b[k][j]
            l.apppend(n)
        matrix.append(l)
    return matrix
