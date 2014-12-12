'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

input is a list of integers representing prices
'''


def max_profit_brute(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if j-i > max_profit:
                max_profit = j-i
    return max_profit


def max_profit(prices):
    troughs = [(prices[0], 0)]
    max_return = 0
    counter = 0
    for e in prices:
        if e < troughs[-1][0]:
            troughs.append((e, counter))
        counter += 1
    for i in range(len(troughs) - 1):
        for e in prices[troughs[i][1]:troughs[(i + 1)][1]]:
            if e - troughs[i][0] > max_return:
                max_return = e - troughs[i][0]
    for e in prices[troughs[-1][1]:]:
        print troughs[-1][1]
        print troughs
        if e - troughs[-1][0] > max_return:
            max_return = e - troughs[-1][0]
    return max_return
