from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = Counter(s1)
        count = len(s1)
        left = 0
        for right in range(len(s2)):
            # 右指標往右移動
            dic[s2[right]] -= 1
            if dic[s2[right]] >= 0:
                count -= 1
            while count == 0:
                # 長度相同代表找到答案
                if right-left+1 == len(s1):
                    return True
                # 左指標往右移動
                dic[s2[left]] += 1
                if dic[s2[left]] > 0:
                    count += 1
                left += 1
        return False
