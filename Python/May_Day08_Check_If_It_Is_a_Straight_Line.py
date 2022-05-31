class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # 取得前兩點座標
        (x1, y1), (x2, y2) = coordinates[:2]
        # 判斷兩向量外積是否為零
        # 公式: (a,b)×(c,d) = a×d−b×c == 0
        for x, y in coordinates:
            if (x2-x1) * (y-y1) - (y2-y1) * (x-x1) != 0:
                return False
        return True