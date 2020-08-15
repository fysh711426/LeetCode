from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def dp(n, m):
            if n == 0:
                return m
            if m == 0:
                return n
            if word1[n-1] == word2[m-1]:
                return dp(n-1, m-1)
            return min(
                dp(n, m-1),    # insert
                dp(n-1, m),    # remove
                dp(n-1, m-1)   # replace
            ) + 1
        return dp(len(word1), len(word2))

        # N, M = len(word1), len(word2)
        # dp = [[0]*(M+1) for _ in range(N+1)]

        # for i in range(N+1):
        #     for j in range(M+1):
        #         if i == 0:
        #             dp[i][j] = j
        #             continue
        #         if j == 0:
        #             dp[i][j] = i
        #             continue

        #         if word1[i-1] == word2[j-1]:
        #             dp[i][j] = dp[i-1][j-1]
        #         else:
        #             dp[i][j] = min(
        #                 dp[i-1][j], dp[i][j-1], dp[i-1][j-1]
        #             ) + 1

        # return dp[-1][-1]