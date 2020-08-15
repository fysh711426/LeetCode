class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = [0]*(num+1)
        for i in range(1, num+1):
            bits[i] = bits[i & (i-1)] + 1
        return bits
        # bits = [0]
        # while len(bits) <= num:
        #     bits.extend([i+1 for i in bits])
        # return bits[:num+1]