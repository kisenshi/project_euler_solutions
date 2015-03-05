"""
PROBLEM 2: Even Fibonacci numbers
"""
# return Fibonacci series up to n but just of those numbers that are even
def fib_even(n):
    result = []
    a, b = 0, 1
    while b < n:
    	if b % 2 == 0:
        	result.append(b)
        a, b = b, a+b
    return result

fib_even_list = fib_even(4000000)
print sum(fib_even_list)