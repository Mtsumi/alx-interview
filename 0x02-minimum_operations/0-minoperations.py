def minOperations(n):
    # Initialize an array to store the minimum number of operations needed to generate i copies of 'H'
    dp = [0] * (n + 1)
    # Initialize the base case for 0 copies of 'H'
    dp[0] = 0
    # Iterate through the array, starting from 1
    for i in range(1, n + 1):
        dp[i] = i  # Initialize the minimum number of operations as i
        j = 2  # Initialize j as 2 (as we can't copy and paste just one H)
        while (j * j <= i):
            if (i % j == 0):
                dp[i] = min(dp[i], dp[j] + dp[i // j])
            j += 1
    return dp[n]
