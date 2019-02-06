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
from _mymodules import abs_error, vector_2norm


def abs_error_2norm(true_value,vector):
    return abs_error(true_value,vector_2norm(vector))

#The code below is used just for testing.
#vector = [5,7,9,2,5]
#print(abs_error_2norm(13.6,vector))


