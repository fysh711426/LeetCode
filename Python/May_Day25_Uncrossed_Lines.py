class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        N, M = len(A), len(B)
        dp = [[0]*(M+1) for _ in range(N+1)]

        for i in range(N):
            for j in range(M):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        return dp[-1][-1]