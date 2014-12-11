'''
The sum of the squares of the first ten natural numbers is 385

The square of the sum of the first ten natural numbers is 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sum_squares(upper_bound):
    '''
    This problem is very straightforward to do in python. It might be difficult
    in other languages that treat integers differently.
    '''
    sum_of_squares = 0
    square_of_sum = 0
    for e in range(1, upper_bound + 1):
        sum_of_squares += e ** 2
        square_of_sum += e
    square_of_sum = square_of_sum ** 2
    return square_of_sum - sum_of_squares

if __name__ == '__main__':
    print(sum_squares(100))
