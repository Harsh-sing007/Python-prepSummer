class StockBuySell:

    def __init__(self, prices):
        self.prices = prices

    def max_profit(self, k):
        n = len(self.prices)

        if n == 0 or k == 0:
            return 0

        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if self.prices[i] > self.prices[i - 1]:
                    profit += self.prices[i] - self.prices[i - 1]
            return profit

        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            max_diff = -self.prices[0]

            for d in range(1, n):
                dp[t][d] = max(dp[t][d - 1],
                               self.prices[d] + max_diff)

                max_diff = max(max_diff,
                               dp[t - 1][d] - self.prices[d])

        return dp[k][n - 1]


# # Driver Code
# if __name__ == "__main__":

#     k = int(input("Enter number of transactions (k): "))
#     prices = list(map(int, input("Enter stock prices: ").split()))

#     obj = StockBuySell(prices)

#     print("Maximum Profit:", obj.max_profit(k))