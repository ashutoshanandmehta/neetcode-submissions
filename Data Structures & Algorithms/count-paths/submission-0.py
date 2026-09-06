class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n)] for _ in range(m)]
        return self.solve(m - 1, n - 1, memo)

    def solve(self, m: int, n: int, memo: list[list[int]]) -> int:

        if m == 0 and n == 0:
            return 1

        if memo[m][n] != 0:
            return memo[m][n]

        if m == 0:
            memo[m][n] = self.solve(m, n - 1, memo)

        elif n == 0:
            memo[m][n] = self.solve(m - 1, n, memo)

        else:
            memo[m][n] = (
                self.solve(m - 1, n, memo)
                + self.solve(m, n - 1, memo)
            )

        return memo[m][n]