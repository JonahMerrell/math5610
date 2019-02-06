'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       January 19 2019
written for:        Homework2 Task2
course:             Math 5610

purpose:            Determine the absolute error of an approximation of the number.
'''

def abs_error(true_value,appr_value):
    abs_error_value = abs(true_value - appr_value)
    return abs_error_value

#The code below is used just for testing.
#print(abs_error(1.0,1.0000132))

