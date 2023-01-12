#!/usr/bin/python3
'''The minimum ops coding challenge
    '''


def minOperations(n):
    # checking if n is a number
    if not isinstance(n, int):
        return 0

    ops_count = 0
    clipboard = 0
    done = 1
    # print('H', end='')
    while done < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            # paste
            done += clipboard
            ops_count += 1
    return ops_count
    # dp = [0] * (n + 1)
    # # Initialize the base case for 0 copies of 'H'
    # dp[0] = 0
    # # Iterate through the array, starting from 1
    # for i in range(1, n + 1):
    #     dp[i] = i  # Initialize the minimum number of operations as i
    #     j = 2  # Initialize j as 2
    #     while (j * j <= i):
    #         if (i % j == 0):
    #             dp[i] = min(dp[i], dp[j] + dp[i // j])
    #         j += 1
    # return dp[n]
