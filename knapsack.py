def knapsack(values, weights, capacity):
    # Number of items
    n = len(values)
    
    # Create a 2D array to store the maximum value that can be obtained for each weight
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the dp array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                # Include the current item and see if the total value is greater
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w-weights[i-1]])
            else:
                # Exclude the current item
                dp[i][w] = dp[i-1][w]
    
    # The maximum value will be in dp[n][capacity]
    return dp[n][capacity]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = knapsack(values, weights, capacity)
print(f"The maximum value that can be obtained is {max_value}")
