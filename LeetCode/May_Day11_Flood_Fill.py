class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 上下左右的偏移量
        dir_r, dir_c = [-1, 1, 0, 0], [0, 0, -1, 1]
        # 圖片長寬
        rlen, clen = len(image), len(image[0])
        # 起始點顏色
        oldColor = image[sr][sc]
        
        def dfs(r, c):
            if image[r][c] != oldColor:
                return
            if image[r][c] == newColor:
                return
            image[r][c] = newColor
            # 往四個方向找色
            for i in range(4):
                # 產生新座標
                nr, nc = r + dir_r[i], c + dir_c[i]
                # 判斷是否超出邊界
                if 0 <= nr < rlen and 0 <= nc < clen:
                    dfs(nr, nc)

        dfs(sr, sc)
        return image