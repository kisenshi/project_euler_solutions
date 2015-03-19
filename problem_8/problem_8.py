"""
PROBLEM 8 : Largest product in a series
"""

SERIES = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
SERIES_LEN = len(SERIES)
PRODUCT_LENGHT = 13
f = open('debug', 'w')

"""
Returns the product of the next X consecutive numbers to have it as reference to be easily to calculate the products during the iteration
If during the calculation a 0 is found, it won't be considered a valid product, so it is skipped the range until the element after the 0 and called again the function
If it is tried to access to a range that it is outside the SERIES, it is returned None
"""
def obtainNextFullProd(start_prod):
    end_prod = start_prod + PRODUCT_LENGHT
    """ It is checked that it is possible to calculate and we are in the range """
    if start_prod >= SERIES_LEN or end_prod > SERIES_LEN:
        return None

    j = start_prod #The iteration to obtain the product starts in the start_prod inserted as parameter
    current_prod = 1 #The current_prod is initialised to 1

    """ It is obtained the product of the X adjacent digits """
    while j < end_prod:
        number = int(SERIES[j]) #current number
        #If the number is a 0, we should start again as the product will not be useful
        if number == 0:
            next_start = j + 1 #The 0 is skipped and the calculus will start again for the following element 
            return obtainNextFullProd(next_start)

        current_prod *= number
        j += 1 #Next element

    #It is needed to return the product obtained, the next index and the index where the product started
    return {"prod" : current_prod, "index" : j, "index_start" : start_prod}

""" 
It returns the largest product of the X adjacent numbers in the SERIES
While the SERIES is iterated, it is considered 3 different cases
1.  There is no product yet, so it is needed to be calculated to be easily to obtain the products
2.  The current number is 0 so the product of it with its adjacent will be 0 so it cannot be considered and it is neede to obtain a new product and keep calculating from the following digit
3.  We have a product as reference and the current number is not 0, we can use the product that it was stored. 
    It would be needed to remove the old digit in SERIES[start_last_prod] as it is not in the range anymore and it will be added the current number to the product
    It is checked if the new product is bigger than tha one stored as the maximum, in which case is replaced
The algorithm keeps going until all the digits in the SERIES has been iterated
"""
def obtainLargestProduct():
    i = 0
    start_last_prod = 0
    full_prod_available = False
    max_prod = 1

    """ We iterate over the whole series """
    while i <= SERIES_LEN:
        number = int(SERIES[i]) #current digit to be considered
        """
        There are 3 cases as it is explained in the header
        """
        if not full_prod_available: 
            """ Not product available yet, it is obtained """
            results = obtainNextFullProd(i)
            if results == None: #No results, no more iteration to do
                break
            i = results["index"]
            start_last_prod = results["index_start"]
            current_prod = results["prod"]
            full_prod_available = True
        elif number == 0: 
            """ 0 is not useful, it is needed to obtain again the product from the next element """
            i += 1
            results = obtainNextFullProd(i)
            if results == None: #No results, no more iteration to do
                break
            i = results["index"]
            start_last_prod = results["index_start"]
            current_prod = results["prod"]
        else:
            """ It is divided by the old number that will not be considered anymore """
            current_prod = current_prod / int(SERIES[start_last_prod])
            start_last_prod += 1
            current_prod *= number
            i += 1

        #If the product obtained for these adjacent digits is bigger, the max is replaced
        if current_prod > max_prod:
            max_prod = current_prod

    return max_prod


solution = obtainLargestProduct()
print "Solution : " + str(solution)