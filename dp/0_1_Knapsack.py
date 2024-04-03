# https://www.youtube.com/watch?v=ntCGbPMeqgg&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=5

def main():
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    result = knapsack(capacity, weights, values, len(weights))
    print(result)


def knapsack(W, wt, val, n):
    dp = [[-1 for j in range(W + 1)] for i in range(n + 1)]

    # Be careful about i, j
    # For example W has 4 elements. starts from 0 to 3
    # when iterating dp table index 1 means weight index 0 as dp index 0 is for caching initial result
    for i in range(n + 1):
        for j in range(W + 1):
            # init start columns
            if i == 0 or j == 0:
                dp[i][j] = 0
                continue

            if wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    val[i - 1] + dp[i][j - wt[i - 1]]
                )
    print(dp)
    return dp[n][W]


if __name__ == "__main__":
    main()
