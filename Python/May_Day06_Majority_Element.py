class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = None
        count = 0

        for n in nums:
            if count == 0:
                x = n
                count = 1
            elif x == n:
                count += 1
            else:
                count -= 1

        return x