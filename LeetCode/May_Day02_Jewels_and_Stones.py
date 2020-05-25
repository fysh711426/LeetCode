class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = set(J)

        count = 0
        for c in S:
            if c in d:
                count = count + 1
        
        return count