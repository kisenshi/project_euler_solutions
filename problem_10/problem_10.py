"""
PROBLEM 10 : Summation of primes
The approach is very similar to the one done in the Problem 7: 10001st prime
It is implemented a function isPrime to check if the current number is divisible by any the previous prime already found. 
If it is not divisible by any of them, we can assure it is prime, so it is increased the sum and added to the list of primes found
Only odd numbers are iterated as 2 is the only even number that will be prime, so we can avoid them and make the calculus a little bit faster
"""

import math

NUMBER = 2000000

"""
Checks if the number is prime or not checking if it can be divided by one of the previous primes already obtained
"""
def isPrime(number, list_of_previous_primes):
	#It has no sense to check the mod with those numbers that are higher than its square root
	number_sqrt = int(math.sqrt(number))

	""" 
	It is iterated over the list_of_previous_primes to check if the number is divisible by any of them
	Only those numbers smaller than the square root of the number are considered
	"""
	for x in list_of_previous_primes:
		if x > number_sqrt:
			#End of the loop, it is impossible to find a divisor from this point
			break
		if number % x == 0:
			#It is not prime as we found a divisor
			return False

	#If the loop has finished it means the number is prime
	return True

"""
It returns the sum of the primes 
"""
def obtainPrimeSum():
	""" We will start the iteration from 3 as it is the first odd number, so if the one that it is requested to obtain is the 1st prime, it is returned 2 """
	if NUMBER == 1:
		return 2

	primes_sum = 2 #It is considered that we already have found 2 so it has been added to the sum
	list_of_previous_primes = [2] #The list of previous primes is initialized with 2

	next_number = 3
	"""
	The algorithm will finish once the NUMBER has been reached as the range we should conisered is finished
	For every prime number found, it is added to the list_of_previous_primes and added to the total sum of primes
	Only odd numbers will be considered, as no other even number apart from 2 will be prime
	"""
	while next_number < NUMBER:
		number = next_number
		#It is checked if is prime
		if isPrime(number, list_of_previous_primes):
			list_of_previous_primes.append(number)
			primes_sum += number

		next_number = number + 2 #Avoiding even numbers

	return int(primes_sum)

"""
Solution
"""

solution = obtainPrimeSum()
print "Solution : " + str(solution)