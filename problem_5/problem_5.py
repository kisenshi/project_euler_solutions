"""
PROBLEM 5: Smallest multiple
It is needed to calculate all the prime factors of all the numbers in the range and choose those that are different, with the biggest exponent
"""
import math

LAST_NUMBER = 20

"""
Returns an array with the prime factors that conforms the number inserted as parameter
"""
def returnPrimeFactors(number):
    prime_factors = [] #The list is initialised to empty
    new_number = number #The new_number should be initialised to the number
    end_loop = False

    """ While not all the prime factors of the number has been obtained, it is needed to keep calm and carry on """
    while not end_loop:
        last_number = number // 2 + 1 #The last number that is possible to be a prime factor (ignoring the number itself) is the number/2

        for x in xrange(2, last_number):
            """ If the number is divisible by the current number, it means it is a prime factor, so it is appended, the new number obtained with the division is calculated and the iteration ends """
            if number % x == 0:
                prime_factors.append(x)
                new_number =  number / x
                break

        """ 
        There are 3 possibilities:
        1. If the last number obtained with the division is 1, it means all the prime factors have been obtained and the loop ends 
        2. The number hasnt change, so no prime factor has been obtained in the last iteration. It means the current number is prime so it should be add as a factor and the loop ends.
        3. It is needed to keep iterating as there are still prime factors to obtain, the number considered in the next iteration will be the last number calculated
        """
        if new_number == 1:
            end_loop = True
        elif new_number == number:
            #It is prime
            prime_factors.append(number)
            end_loop = True
        else:
            number = new_number

    #The calculation has finished and the array with the prime factors of the number is returned (please note that we dont take into consideration 1 as it wont be useful for our further calculation)
    return prime_factors

"""
Returns a dictionary that contains all the unique prime factors for all the numbers in the range and the max exponent for each of them that has to be considerated to make the calculation
{factor1: exponent1, factor2: exponent2 ...}
"""
def obtainFactorsAndExponents():
    different_factors = [] #Initialised to empty
    factors_exponents = {} #Initialised to empty

    """ It is iterated over all the numbers in the range [1, LAST_NUMBER] """
    for x in xrange(1, LAST_NUMBER + 1):
        n_factors = returnPrimeFactors(x) #It is obtained the list with all the prime factors
        n_factors_unique = list(set(n_factors)) #To iterate and check if they are already in the dictionary, it is easy if the list contains not repated factors

        """ It is iterate over all the unique factors, check their exponent (counting the number of times they appear in the list) and added to the dictionary if they are not already """
        for factor in n_factors_unique:
            exponent = n_factors.count(factor) #The exponent of the prime factor is obtained counting how many times it appears in the list

            """
            If the factor is already in the list, it is needed to check the current exponent considered for that numbers:
            1. If the current exponent in the dictionary is smaller, it is needed to change it and the new exponent is set. 
            2. If not, nothing else is done. The algorithm keeps going
            If the factor is not in the list, it is inserted and the exponent is added to the dictionary as well
            """
            if factor in different_factors:
                current_exponent = factors_exponents[factor]
                if exponent > current_exponent:
                    factors_exponents[factor] = exponent
            else:
                different_factors.append(factor)
                factors_exponents[factor] = exponent

    #It is returned the complete dictionary
    return factors_exponents

"""
Returns the smallest multiple
It is called the obtainFactorsAndExponents function, which returns the dictionary conformed by the factors and their exponents 
The smallest multiple is obtained multiplying all the factors powed to their exponent: (factor1 ^ exponent1) * (factor2 ^ exponent2) * .... * (factorn ^ exponentn)
"""
def obtainSmallestMultiple():
    factors_exponents = obtainFactorsAndExponents()

    smallest_multiple = 1 #The smallest multiple is initialised to 1
    """We iterate over the elements in the dictionary to obtain the multiple"""
    for factor, exponent in factors_exponents.iteritems():
        smallest_multiple *= pow(factor, exponent)

    #The smallest multiple is returned
    return smallest_multiple


"""
Solution
"""

smallest_multiple = obtainSmallestMultiple()
print "Solution: " + str(smallest_multiple)
