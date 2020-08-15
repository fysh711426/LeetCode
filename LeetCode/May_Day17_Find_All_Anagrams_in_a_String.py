from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcount = Counter(p)
        scount = Counter(s[:len(p)])
        result = [0] if pcount == scount else []
        for i in range(len(s)-len(p)):
            # 開頭往右一格
            scount[s[i]] -= 1
            if scount[s[i]] == 0: 
                del scount[s[i]]
            # 結尾往右移一格
            scount[s[i+len(p)]] += 1
            if pcount == scount:
                result.append(i+1)
        return result
        