'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       January 19 2019
written for:        Homework2 Task3
course:             Math 5610

purpose:            Determine the relative error of an approximation of the number.
'''

def calc_rel_error(true_value,appr_value):
    rel_error = abs((true_value - appr_value)/true_value)
    return rel_error

#The code below is used just for testing.
print(calc_rel_error(1.0,1.0000132))

