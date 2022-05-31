class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 產生圖形鄰接表
        graph = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            graph[j].append(i)
        
        # 狀態:
        # 0: 初始狀態、1: 臨時標記、2: 永久標記
        node = [0] * numCourses

        # 使用 DFS 檢查是否存在循環
        def dfs(n):
            if node[n] == 1:
                return True
            if node[n] == 2:
                return
            node[n] = 1
            for i in graph[n]:
                if dfs(i) == True:
                    return True
            node[n] = 2
        
        # 搜尋所有未被標記的節點
        for i in range(len(node)):
            if node[i] == 0:
                if dfs(i) == True:
                    return False
        return True