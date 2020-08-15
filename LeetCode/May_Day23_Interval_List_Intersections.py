class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        rlt = []
        i = j = 0
        while i < len(A) and j < len(B):
            start = max(A[i][0], B[j][0])
            end   = min(A[i][1], B[j][1])
            # 線段有交集就加入結果
            if start <= end:
                rlt.append([start, end])
            # 將排在前的線段索引加一
            if A[i][1] > B[j][1]: 
                j += 1
            else: 
                i += 1
        return rlt