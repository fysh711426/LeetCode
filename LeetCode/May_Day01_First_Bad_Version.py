# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        return self.search(1, n + 1)
        
    def search(self, start, end):
        half = int((end - start) / 2) + start
        if isBadVersion(half) is False:
            return self.search(half + 1, end)
        if isBadVersion(half - 1) is True:
            return self.search(start, half)
        return half