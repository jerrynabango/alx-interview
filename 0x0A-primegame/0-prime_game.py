#!/usr/bin/python3
"""Defines an Epic Prime Game"""


def isWinner(x, nums):
    """name of the player that won the most rounds"""
    if x < 1 or not nums:
        return None
    maria, ben = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, isPrime in enumerate(primes, 1):
        if i == 1 or not isPrime:
            continue
        for y in range(i + i, n + 1, i):
            primes[y - 1] = False
    for _, n in zip(range(x), nums):
        primesCount = len(list(filter(lambda x: x, primes[0: n])))
        ben += primesCount % 2 == 0
        maria += primesCount % 2 == 1
    if maria == ben:
        return None
    return 'Maria' if maria > ben else 'Ben'
