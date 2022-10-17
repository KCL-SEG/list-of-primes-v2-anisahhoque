"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    listprime = []
    if number_of_primes <= 0:
        raise ValueError
    for x in range(2,10000000):
        for y in range(2,x):
            if x%y==0:
                break
        else:  
            listprime.append(x)

            if len(listprime) == int(number_of_primes):
                break

    return listprime
