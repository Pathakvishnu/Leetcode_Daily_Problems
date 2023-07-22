class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                      (2, 1), (2, -1), (-2, 1), (-2, -1)]

        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1

        for moves in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for direction in directions:
                        prev_i, prev_j = i - direction[0], j - direction[1]
                        if 0 <= prev_i < n and 0 <= prev_j < n:
                            dp[moves][i][j] += dp[moves - 1][prev_i][prev_j]

                    dp[moves][i][j] /= 8

        total_probability = sum(
            dp[k][i][j]
            for i in range(n)
            for j in range(n)
        )
        return total_probability

n = 3
k = 2
row = 0
column = 0

obj = Solution()
obj.knightProbability(n,k,row,column)

