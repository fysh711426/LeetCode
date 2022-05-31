class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # 產生圖形鄰接表
        graph = [[] for _ in range(N)]
        for a, b in dislikes:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)

        # 狀態:
        # 0: 初始狀態、1: 群組一、2: 群組二
        node = [0] * N
        
        # 使用 DFS 分配群組
        def dfs(n, g):
            if node[n] != 0:
                return node[n] == g
            node[n] = g
            for i in graph[n]:
                if dfs(i, g%2+1) == False:
                    return False
        
        # 搜尋所有未被分組的節點
        for i in range(len(node)):
            if node[i] == 0:
                if dfs(i, 1) == False:
                    return False
        return True