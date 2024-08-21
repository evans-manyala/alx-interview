#!/usr/bin/python3
"""
Function to solve a problem of determining the fewest number
of coins needed to meet a given total.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    numCoins = [total + 1] * (total + 1)
    numCoins[0] = 0

    for coin in sorted(coins, reverse=True):
        for i in range(coin, total + 1):
            numCoins[i] = min(numCoins[i], numCoins[i - coin] + 1)

    return numCoins[total] if numCoins[total] != total + 1 else -1
