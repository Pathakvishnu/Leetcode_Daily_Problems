class WordNode:
    def __init__(self):
        self.children=dict()
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for w in word:
            if not ptr.children.get(w,0):
                ptr.children[w]=WordNode()
            ptr = ptr.children[w]

        ptr.end=True

    def search(self, word: str) -> bool:
        stack = [(self.root,word)]
        while stack:
            node, w = stack.pop()
            if not w:
                if node.end:
                    return True
            elif w[0]=='.':
                for n in node.children.values():
                    stack.append((n,w[1:]))
            else:
                if w[0] in node.children:
                    n = node.children[w[0]]
                    stack.append((n,w[1:]))
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)