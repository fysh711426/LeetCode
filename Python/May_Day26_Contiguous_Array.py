class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        c, m, dic = 0, 0, { 0: -1 } 
        for i in range(len(nums)):
            c += -1 if nums[i] == 0 else 1
            if c in dic:
                m = max(m, i-dic[c])
            else:
                dic[c] = i
        return m