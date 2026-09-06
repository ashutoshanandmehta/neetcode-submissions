class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        if n == 0:
            return 0

        memo = [[-1 for _ in range(amount + 1)]
                for _ in range(n + 1)]

        for i in range(n + 1):
            memo[i][0] = 1

        return self.solve(amount, coins, n, memo)

    def solve(self, amount: int, coins: List[int],
              n: int, memo: List[List[int]]) -> int:

        if n == 0:
            return 0

        if memo[n][amount] != -1:
            return memo[n][amount]

        dont_take = self.solve(amount, coins, n - 1, memo)
        take = 0
        if coins[n - 1] <= amount:
            take = self.solve(
                amount - coins[n - 1],
                coins,
                n,
                memo
            )

        memo[n][amount] = dont_take + take

        return memo[n][amount]