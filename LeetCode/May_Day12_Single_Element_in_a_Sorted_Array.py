class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def search(start, end):
            mid = ((end - start) // 2) + start
            if start == end:
                return nums[start]
            if nums[mid] == nums[mid^1]:
                return search(mid+1, end)
            return search(start, mid)
        return search(0, len(nums)-1)
        # temp = 0
        # for n in nums:
        #     temp ^= n
        # return temp