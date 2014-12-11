'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


def is_prime(integer):
    '''
    For ints 25 or smaller, the number is checked against a short list of
    primes. For larger ints, the function first checks if the int is divisible
    by 2 or 3. If not, the function tests if it is divisible by every other
    number that isn't divisible by 2 or 3 that is smaller that the original
    integer's square root. I ended up going a different direction with this
    problem, but I'm still happy with this function so I'll keep it here
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


def greatest_prime_factor(value):
    counter = 2
    largest = 0
    while counter <= value ** 0.5:
        if value % counter == 0:
            value /= counter
            largest = counter
        else:
            if counter == 2:
                counter = 3
            else:
                counter += 2
    if largest > value:
        return largest
    else:
        return value

if __name__ == '__main__':
    print(greatest_prime_factor(600851475143))
