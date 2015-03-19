"""
PROBLEM 4: Largest prime factor
"""

INITIAL_NUMBER = 999
LAST_NUMBER = 100
f = open('palindrome_products', 'w')

"""
Checks if a number is palindromic or not.
A number is palindromic if it is read the same both ways
"""
def isPalindromic(number):
	#It will be considered as string to be able to treat it
	number_str = str(number)

	first_i = 0
	last_i = len(number_str) - 1

	while first_i < last_i:
		if int(number_str[first_i]) != int(number_str[last_i]):
			#If the numbers considered are not equal, is not palindrome, it has no sense to continue, it is returned false
			return False

		""" If both current numbers considered were equal, it is still possible that the number is palindromic, we keep checking """
		first_i += 1
		last_i -= 1

	#If the loop finished it means all the checking was successfull, so it is returned true
	return True

"""
Returns the largest palindrome product. It obtains all the products for 3 digit factors and, checking if it is palindromic or not, it returns the largest one.
I am sure it can be optimized someway and stop the loop at a secure point, but I am thinking which would be a secure cut to make sure the largest palindromic number is returned
"""
def obtainLargestPalindromicProduct():
	""" Both factors are initialised """
	factor_1 = INITIAL_NUMBER
	factor_2 = INITIAL_NUMBER

	largest_palindromic = 0 #the largest palindromic is initialised to 0
	while factor_2 >= LAST_NUMBER: #While there are still numbers to calculate
		#Print to be aware about what is going on
		print "Factor 1: "+str(factor_1)+" Factor 2: "+str(factor_2)

		#It is obtained the product
		product = factor_1 * factor_2

		""" It is checked if the product is palindromic and, if it is and it is largest than the current one considered, it is replaced """
		if isPalindromic(product):
			f.write("PALINDROMIC => Factor 1: "+str(factor_1)+" Factor 2: "+str(factor_2)+" product: "+str(product)+"\n")
			if product > largest_palindromic:
				largest_palindromic = product

		""" It is obtained the next factors to be used in the loop """
		if(factor_1 == factor_2):
			factor_1 = INITIAL_NUMBER
			factor_2 -= 1
		else:
			factor_1 -= 1

	return largest_palindromic

"""
Solution
"""

solution = obtainLargestPalindromicProduct()
print solution
