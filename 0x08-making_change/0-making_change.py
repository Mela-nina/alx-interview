#!/usr/bin/python3
"""
This is Making Change
"""


def makeChange(coins, total):
    """
    This returns the minimum number of coins needed to meet a given total
    Args:
        coins (list of ints): a list of coins of different values
        total (int): total value to be met
    Return:
        Number of coins or -1 if meeting the total is not possible
    """
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        s = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coin_count = 0
    for t in coins:
        if total % t == 0:
            coin_count += int(total / t)
            return coin_count
        if total - t >= 0:
            if int(total / t) > 1:
                coin_count += int(total / t)
                total = total % t
            else:
                coin_count += 1
                total -= t
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_count
