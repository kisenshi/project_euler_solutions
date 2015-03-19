"""
PROBLEM 3: Largest prime factor
"""

import math

NUMBER = 600851475143

"""
It is returned the largest prime factor of the number inserted.

Going through all the odd numbers (and the 2 as it is prime) in the range (2, number/2) it is checked if the number is divisible by each of them.
If the number is divisible, it is obtained the result of the division obtaining a big divisor of the number. If this big divisor is prime, we would have our solution.

To check if it is prime or the algorithm should keep running, it is recursively obtained the big divisors of each of them until the number considered's biggest divisor is itself;
which would mean that it is prime and, as result, the number we were looking for
"""
def obtainLargePrime(number):
	print "number: " + str(number)
	divisor = 1
	last_number = int(math.ceil(number / 2)) #It has no sense to go through the numbers that are bigger than the number/2 as they will never be a solution

	x = 2 #It is needed to start with 2 as 1 will always be a divisor but we are not interested on it, for obvious reasons
	while x <= last_number: #While it has sense to still looking for divisors
		if number % x == 0: #If the number considered is divisible by the current number, we can obtain the biggest divisor to be able to keep calculating 
			divisor = int(number / x) #We obtain the biggest divisor and the loop can be finished to be able to continue with the algorithm, we are not interested in this loop anymore
			break

		if x == 2: #2 is the only even number we will be interested on, as the rest of them are not prime
			x += 1 #If we are in 2, we need to just increase 1 to start going through the odd numbers, the only ones we will be interested on
		else:
			x += 2 #If we are already checking the odd numbers, we increase 2 to avoid the even numbers ans try to find prime divisors

	"""If the loop has finished and any prime number to divide the current number is found, it means it is prime itself so we will return it"""
	if divisor == 1:
		return number

	""" Just some printing to be aware about what is happening """
	print "divisor: " + str(divisor)
	print " "

	""" 
	Ok, we found a divisor, a big one, but there is a big chance that this is not the prime number we are looking for yet, we need to repeat the process with it
	The last number returned will be our solution
	"""
	return obtainLargePrime(divisor)


solution = obtainLargePrime(NUMBER)

print " "
print "Solution: " + str(solution)