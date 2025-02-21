class RandomizedSet:
    def __init__(self):
        self.lst = []
        self.indexMap = {}

    def insert(self, val: int) -> bool:
        if val in self.indexMap:
            return False
        self.lst.append(val)
        self.indexMap[val] = len(self.lst) -1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexMap:
            return False
        index = self.indexMap[val]
        self.lst[index] = self.lst[-1]
        self.indexMap[self.lst[-1]] = index
        self.lst.pop()
        del self.indexMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()