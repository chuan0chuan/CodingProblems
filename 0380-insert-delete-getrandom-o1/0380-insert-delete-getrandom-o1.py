class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.valIndexMap = {}

    def insert(self, val: int) -> bool:
        if val in self.valIndexMap:
            return False
        self.lst.append(val)
        self.valIndexMap[val] = len(self.lst) - 1 
        return True

    def remove(self, val: int) -> bool:
        # cause regular remove for list is o(n), so we need swap and pop()
        if val not in self.valIndexMap:
            return False
        index = self.valIndexMap[val]
        self.lst[index] = self.lst[-1] 
        self.valIndexMap[self.lst[-1]]  = index
        self.lst.pop()
        del self.valIndexMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()