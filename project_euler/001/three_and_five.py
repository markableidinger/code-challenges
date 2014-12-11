"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def three_and_five(upper_bound):
    '''
    iterates over all numbers from 1 to upper_bound, adding each one that is
    a multiple of 3 or 5 to the variable "total". Returns total. Complexity of O(n).
    '''
    total = 0
    for i in range(1, upper_bound):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

if __name__ == '__main__':
    print(three_and_five(1000))
