"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def is_prime(integer):
    '''
    For ints 25 or smaller, the number is checked against a short list of
    primes. For larger ints, the function first checks if the int is divisible
    by 2 or 3. If not, the function tests if it is divisible by every other
    number that isn't divisible by 2 or 3 that is smaller that the original
    integer's square root.
    '''
    #for small numbers, just check against a short list of known primes
    if integer <= 25:
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        if integer in small_primes:
            return True
        else:
            return False
    else:
        #check if the number is divisible by 2 or 3
        if integer % 2 == 0 or integer % 3 == 0:
            return False
        factor = 5
        while factor <= integer ** 0.5:
            #for every 6 integers, 2 are not divisible by 2 or 3. This loop
            #checks those 2 numbers in every group of 6
            if integer % factor == 0 or integer % (factor + 2) == 0:
                return False
            factor += 6
        return True


def prime_factorization_list(integer):
    '''
    This function goes through all of the possible prime factors of a number
    and returns a list of them. Because this is a prime factorization, each
    factor can occur more than once
    '''
    newint = integer
    if newint < 2:
        return []
    else:
        counter = 2
        factors = []
        while counter <= newint ** 0.5:
            if newint % counter == 0:
                newint /= counter
                factors.append(counter)
            else:
                if counter == 2:
                    counter = 3
                else:
                    counter += 2
        if newint > 1:
            factors.append(newint)
        return factors


def prime_factorization_dict(integer):
    '''
    This function goes through all of the possible prime factors of a number
    and returns a dictionary of them, with each key being a prime factor and
    each value being the number of times it occurs in the prime factorization
    '''
    newint = integer
    if newint < 2:
        return {}
    else:
        counter = 2
        factors = {}
        while counter <= newint ** 0.5:
            if newint % counter == 0:
                newint /= counter
                if factors.get(counter, None) is None:
                    factors[counter] = 1
                else:
                    factors[counter] += 1
            else:
                if counter == 2:
                    counter = 3
                else:
                    counter += 2
        if newint > 1:
            if factors.get(newint, None) is None:
                factors[newint] = 1
            else:
                factors[newint] += 1
        return factors


def evenly_divisible_by_range(upper_bound):
    '''
    using prime_factorization_dict() on each number from 1/2 of the upper bound
    to the upper bound, this function determines the prime factorization of the solution
    '''
    all_factors = {}
    for i in range(upper_bound / 2 + 1, upper_bound + 1):
        current_factors = prime_factorization_dict(i)
        for key, value in current_factors.items():
            if all_factors.get(key, None) is None:
                all_factors[key] = value
            elif all_factors[key] < value:
                all_factors[key] = value
    evenly_divided = 1
    for factor, amount in all_factors.items():
        evenly_divided *= (factor ** amount)
    return evenly_divided

if __name__ == '__main__':
    print(evenly_divisible_by_range(20))
