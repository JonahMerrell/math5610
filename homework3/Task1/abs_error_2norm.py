'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       february 5 2019
written for:        Homework3 Task1
course:             Math 5610

purpose:            Implement a method that returns the absolute error in the approximation of one vector by another when the 2-norm is used
'''
import math

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import vector_2norm, vector_add, vector_scal_mult


def abs_error_2norm(true_vector,appr_vector):
    abs_error = vector_2norm(vector_add(true_vector,vector_scal_mult(-1,appr_vector)))
    return abs_error

#The code below is used just for testing.
#vector1 = [5,7,9,2,5]
#vector2 = [5.1,7.2,8.7,2,5.15]
#print(abs_error_2norm(vector1,vector2))


