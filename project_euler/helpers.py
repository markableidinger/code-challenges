'''
This is a module where I put all of the useful helper functions I make
for project euler problems.
'''

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


def make_prime_list(upper_bound):
    '''
    This funciton find all primes from 1 to the given argument. This is done by iterating
    over all numbers that are not mutiples of 2 or 3 and appending them to a
    list which is the returned. Depends on is_prime()
    '''
    if upper_bound < 2:
        return []
    else:
        primes_in_range = [2]
        counter = 3
        while counter <= upper_bound:
            if is_prime(counter):
                primes_in_range.append(counter)
            if (counter + 2) % 3 == 0:
                counter += 4
            else:
                counter += 2
        return primes_in_range


def prime_factorization_list(integer):
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
