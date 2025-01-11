def main():
    values = [2, 3, 7, 8, 10]
    final_value = 11

    result = subset_sum(values, final_value)

    print(f"Subset sum present: {result}")


def subset_sum(values, final_value):
    arr_len = len(values)
    dp = [[False] * (final_value + 1) for _ in range(arr_len + 1)]
    dp[0][0] = True

    for dp_i in range(1, arr_len + 1):
        for dp_j in range(final_value + 1):

            if values[dp_i - 1] > dp_j:
                dp[dp_i][dp_j] = dp[dp_i - 1][dp_j]
                continue

            dp[dp_i][dp_j] = dp[dp_i - 1][dp_j] or dp[dp_i - 1][dp_j - values[dp_i - 1]]

    for row in dp:
        print(row)

    return dp[-1][-1]


if __name__ == "__main__":
    main()
