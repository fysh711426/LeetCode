class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 圖片長寬
        rlen, clen = len(image), len(image[0])
        # 起始點顏色
        oldColor = image[sr][sc]
        
        def dfs(r, c):
            # 判斷是否超出邊界
            if r < 0 or r >= rlen or c < 0 or c >= clen:
                return
            # 檢查顏色是否和起始點相同
            if image[r][c] != oldColor:
                return
            # 檢查是否已填色過
            if image[r][c] == newColor:
                return
            # 修改顏色
            image[r][c] = newColor
            # 往四個方向移動中心點
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r, c+1)

        dfs(sr, sc)
        return image