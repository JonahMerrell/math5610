'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       January 9 2019
written for:        Problem Set 1
course:             Math 5610

purpose:            Determine a machine epsilon for the computers I would like
                    work on computationally. The code contains 2 subroutines.

                     smaceps - returns the single precision value for machine precision
                     dmaceps - returns the double precision value for machine precision
'''

def calculate_double_float_precision():
    y = 1.0
    x = 1.0
    z = x + y

    error = abs(z - x)
    iteration_count = 0

    while (error > 0):
        y = y/2
        z = x + y
        error = abs(z - x)
        iteration_count += 1

    return [iteration_count,y]




#The code below is used just for testing.
#dmaceps_data = calculate_double_float_precision()
#print("machine double float mantissa = " + str(dmaceps_data[0]))
#print("machine double float precision = " + str(dmaceps_data[1]))




