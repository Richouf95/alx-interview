#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Make Change
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make 0 amount

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity,
    # it means it's not possible to make the total with the given coins
    return dp[total] if dp[total] != float('inf') else -1
