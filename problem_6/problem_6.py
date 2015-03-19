"""
PROBLEM 6: Sum square difference
It is needed to calculate all the prime factors of all the numbers in the range and choose those that are different, with the biggest exponent
"""

LAST_NUMBER = 100

"""
Returns the difference between the sum of the squares of the natural numbers in the range [1, LAST_NUMBER] and the square of the sum
"""
def obtainSumSquareDifference():
    n_squares_sum = 0 #It will store the sum of the squares of the numbers in the range
    n_sum = 0 #It will store the sum of the numbers in the range

    """ To avoid going through the whole range twice, it is calculated both the sum and the square at rthe same time"""
    for x in xrange(1, LAST_NUMBER + 1):
        n_sum += x
        n_squares_sum += x*x

    #It is obtained the square of the sum to be able to obtain the difference
    n_sum_square = n_sum * n_sum

    #It is returned the difference
    return n_sum_square - n_squares_sum


"""
Solution
"""
solution = obtainSumSquareDifference()
print "Solution: " + str(solution)