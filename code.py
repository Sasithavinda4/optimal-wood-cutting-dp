def wood_cutting_with_order(L, cuts) : 
    # Include endpoints for the cuts array 
    cuts = [0] + sorted(cuts) + [L] 
    n = len(cuts) 
     
    # Initialize the DP table (Cost table & Order table) 
    dp = [[0] * n for _ in range(n)] 
    order = [[None for _ in range(n)] for _ in range(n)] 
 
    # Fill the DP table for lengths from 2 to n 
    for length in range(2, n) : 
        for i in range(n - length) : 
            j = i + length 
            dp[i][j] = float('inf') 
            # Try all possible cuts 
            for k in range(i + 1, j): 
                cost = dp[i][k] + dp[k][j] + cuts[j] - cuts[i] 
                if cost < dp[i][j]: 
                    dp[i][j] = cost 
                    # Record the index 
                    order[i][j] = k 
 
    # Get the order of cuts 
    def get_cut_order(i, j) : 
        if order[i][j] is None : 
            return [] 
        k = order[i][j] 
        return get_cut_order(i, k) + [cuts[k]] + get_cut_order(k, j) 
     
    # Return the minimum cost and the sequence of cuts 
    return dp[0][n - 1] , get_cut_order(0, n - 1)