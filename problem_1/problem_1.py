"""
PROBLEM 1: Multiples of 3 and 5
"""

"""
SOLUTION 1: 
Loop through the range of numbers. check if they are multiples and add to the sum if they are
"""
LAST_NUMBER = 1000

def solutionOne():
	sum_sol_1 = 0
	for x in xrange(1,LAST_NUMBER):
		if (x % 3 == 0) | (x % 5 == 0):
			sum_sol_1 += x

	print sum_sol_1

"""
SOLUTION 2: 
Loop through the range of numbers between 1 and (1000 / LAST_NUMBER) as it is not needed to go through all of them to be able to obtain the sum of 3 and 5 multiples
In each element in the range considered, it is increased the total sum considering its 3 and 5 multiples, that will be in the range (because our range is much smaller in this case)
"""
def solutionTwo():
	sum_sol_2 = 0
	last_number_3 = LAST_NUMBER // 3 #floor division
	last_number_5 = LAST_NUMBER // 5 #floor division

	for x in xrange(1, last_number_3 + 1):
		#If the current number considered it is bigger than the last number to consider for 5, it is skipped its calculus
		if x < last_number_5:
			mult_five = x * 5
			sum_sol_2 += mult_five

		#For the multiples of 3 calculation, it is skipped those that were already multiple of 5 to not considered them twice in the sum
		if x % 5 != 0:
			mult_three = x * 3 
			sum_sol_2 += mult_three

	print sum_sol_2


"""
Both solutions are executed calculating the time it taked to obtain the result
"""

import time

start_time = time.time()
solutionOne()
print("--- Solution 1: %s seconds ---" % (time.time() - start_time))

start_time = time.time()
solutionTwo()
print("--- Solution 2: %s seconds ---" % (time.time() - start_time))
