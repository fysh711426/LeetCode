class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # 使用 Kadane's 演算法
        maxL = maxG = A[0]
        minL = minG = A[0]
        for i in range(1, len(A)):
            n = A[i]
            maxL = max(maxL + n, n)
            maxG = max(maxL, maxG)
            minL = min(minL + n, n)
            minG = min(minL, minG)
        # 另外處理 minG 包含整個陣列的情況
        total = sum(A)
        if minG == total:
            return maxG
        return max(maxG, total-minG)