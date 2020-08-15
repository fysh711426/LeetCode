from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        result = ""
        for key, value in counter.most_common():
            result += key * value
        return result