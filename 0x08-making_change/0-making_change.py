#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    few = 0
    count = 0
    coins.sort(key=lambda x: x, reverse=True)
    while coins:
        value = coins[0]
        if few + value > total:
            coins.pop(0)
            continue
        few += value
        count += 1
        if few == total:
            return count
    return -1
