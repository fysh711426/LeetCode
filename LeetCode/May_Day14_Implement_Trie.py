class Node:
    def __init__(self):
        self.count = 0
        self.next = {}

class Trie:

    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str) -> None:
        temp = self.root
        for c in word:
            if c not in temp.next:
                temp.next[c] = Node()
            temp = temp.next[c]
        temp.count += 1
        
    def search(self, word: str) -> bool:
        temp = self.root
        for c in word:
            if c not in temp.next:
                return False
            temp = temp.next[c]
        return temp.count > 0
        
    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for c in prefix:
            if c not in temp.next:
                return False
            temp = temp.next[c]
        return True