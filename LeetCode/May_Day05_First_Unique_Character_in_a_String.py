class Solution:
    def firstUniqChar(self, s: str) -> int:
        mark = [0] * 26

        # 紀錄次數
        for c in s:
            mark[ord(c) - ord('a')] += 1
        
        # 取出字母進行判斷
        for c in s:
            if mark[ord(c) - ord('a')] == 1:
                return s.index(c)
        return -1