from libcpp.vector cimport vector

cdef extern from "scalarAdd.h":
    int sum_my_vector(vector[int] my_vector)

def scalarAdd(my_list):
    cdef vector[int] my_vector = my_list
    return sum_my_vector(my_vector)