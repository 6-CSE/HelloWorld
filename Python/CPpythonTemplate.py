def knapsack(limit, values, weights):
    """Returns the maximum value that can be reached using given weights"""
    n = len(weights)
    dp = [0]*(limit+1)
    for i in range(n):
        for j in range(limit, weights[i]-1, -1):
            dp[j] = max(dp[j], values[i] + dp[j - weights[i]])
    return dp[-1]
  
  
