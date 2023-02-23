#!/usr/bin/python3
"""
"""
# from typing import List


def makeChange(coins, total):
    """Module to find the minimum number of coins
    needed to meet a given amount
    Solution uses dynamic programming
    """
    if total < 1:
        return 0

    # creating a 2D array for memoization
    memo = [[0] * (total + 1) for _ in range(len(coins))]

    # looping over the memo 2D array to fill it with values

    for i in range(len(coins)):
        for j in range(1, total + 1):
            if i == 0:
                memo[i][j] = j // coins[i]
            elif j < coins[i]:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = min(memo[i - 1][j], 1 + memo[i][j - coins[i]])

    return memo[-1][-1] if memo[-1][-1] != float('inf') else -1
