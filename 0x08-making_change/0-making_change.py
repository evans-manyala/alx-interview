#!/usr/bin/python3
"""
Function to solve a problem of determining the fewest number
of coins needed to meet a given total.
"""


def makeChange(coins, total):
    """
    Return the fewest number of coins needed to meet a given total
    Return:
        Number of coins or -1 if meeting the total is not possible
    """
    if total <= 0:
        return 0
    if not coins:
        return -1
    # Ensure all coin values are positive
    if any(coin <= 0 for coin in coins):
        return -1

    # Sort coins in descending order for efficiency
    coins.sort(reverse=True)

    # Initialize DP array
    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    # Fill the DP array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the result
    return dp[total] if dp[total] != float("inf") else -1
