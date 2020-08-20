''':arg
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
num = [2, 4, 1]


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int

    사고나서 팔아야한다.
    """
    max_profit, min_price = 0, float('inf')

    for price in prices:
        min_price = min(min_price, price)
        print(min_price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit


print(maxProfit(num))

Input = [2, 4, 1]


def maxProfit(prices):
    min_price = min(prices)
    min_idx = 0
    re_prices = []

    for n, p in enumerate(prices):
        if prices[-1] == min_price:
            return 0

        if min_price == p:
            min_idx = n

    for n, p in enumerate(prices):
        if min_idx < n:
            re_prices.append(p)

    max_price = max(re_prices)

    return max_price - min_price


print(maxProfit(Input))
