class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda it: it[0]**2 + it[1]**2)
        return points[:K]