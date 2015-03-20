"""
PROBLEM 9 : Special Pythagorean triplet
Making some basic calculus we obtain that

c = sqrt(a^2 + b^2)
a = (500000 - 1000b)/(1000-b)

We know that all the numbers are in the range [1, 998] so we will start assigning b with different values until we obtain a valid a and a valid c
"""

import math

"""
Given a possible b, it is returned a valid a for it
If for the given b there is no valid a, it is returned None
Making some basic maths clearing up a and b, we obtained the following statement:
a = (500000 - 1000b)/(1000-b)
Please note that a is an integer so the dividend has to be divisible by the dividing and it cannot be a negative number
"""
def obtainAgivenB(b):
	dividend = 500000 - 1000*b
	dividing = 1000 - b

	#If it is not divisible or the dividend it is not bigger than 0, there is no valid a for this b
	if dividend % dividing != 0 or dividend < 0:
		return None

	#It is returned the valid a
	return dividend / dividing

"""
Given two valid a and b, it is needed to obtain the valid c
We know that:
c = sqrt(a^2 + b^2)
"""
def obtainCgivenAandB(a, b):
	a_pow = pow(a, 2)
	b_pow = pow(b, 2)
	c = math.sqrt(a_pow + b_pow)

	return c

"""
It is checked that the a, b and c numbers obtained are correct and the sum is valid
1000 = a + b + c
"""
def sumIsValid(a, b, c):
	sum = a + b + c
	if sum == 1000:
		return True

	return False

"""
It is obtained the Pythagorean triplet
It is iterated over the range [1, 998] assigning each number to b and trying to get a valid a and c from each value
At the moment that a valid a and c are found, it is returned the product of a*b*c
"""
def obtainPythagoreanTriplet():
	for b in xrange(1, 999):
		#It is tried to obtain the valid a for the current b
		a = obtainAgivenB(b)
		if a == None: #Not valid a found, let's check the next b
			continue

		#It is obtained the valid c for the current x
		c = obtainCgivenAandB(a, b)

		#It is checked that the three numbers are valid checking their sum
		if sumIsValid(a, b, c):
			return a * b * int(c)

"""
Solution
"""

solution = obtainPythagoreanTriplet()
print "Solution : " + str(solution)
