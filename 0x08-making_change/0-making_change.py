#!/usr/bin/python3
"""
A change comes from within
"""


def makeChange(coins, total):
    """
    When given a pile of coins of different values,
    determine the fewest number of coins needed to
    meet a given amount total
    """
    if total <= 0:
        return 0
    dp = [0] + [float("inf")] * (total)
    for coin in coins:
        for a in range(coin, total + 1):
            dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[-1] if dp[-1] != float("inf") else -1
