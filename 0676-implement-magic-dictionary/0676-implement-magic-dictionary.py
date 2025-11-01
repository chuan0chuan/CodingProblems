class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class MagicDictionary:
    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

    def search(self, searchWord: str) -> bool:
        def dfs(node, i, modified):
            if i == len(searchWord):
                return modified and node.is_end
            
            ch = searchWord[i]
            
            for c, nxtnode in node.children.items():
                if c == ch:
                    if dfs(nxtnode, i +1, modified):
                        return True
                else:
                    if not modified and dfs(nxtnode, i + 1, True):
                        return True
            return False
        return dfs(self.root, 0 ,False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)