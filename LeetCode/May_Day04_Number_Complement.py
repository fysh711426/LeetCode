class Solution:
    def findComplement(self, num: int) -> int:
        # 1
        mask = 1

        # 1000 > 101
        while mask <= num:
            mask = mask << 1
        
        # 10 = 1000 - 101 - 1
        return mask - num - 1