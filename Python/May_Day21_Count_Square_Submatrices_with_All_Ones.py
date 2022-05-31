class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        M = len(matrix[0])
        dp = [[0] * M for _ in range(N)]

        count = 0
        for i in range(N):
            for j in range(M):
                dp[i][j] = matrix[i][j]
                if i and j and matrix[i][j]:
                    dp[i][j] = min(
                        dp[i-1][j-1], dp[i-1][j], dp[i][j-1]
                    ) + 1
                count += dp[i][j]

        return count