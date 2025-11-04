class RandomizedCollection:

    def __init__(self):
        self.nums =[]
        self.pos = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.pos[val].add(len(self.nums) - 1)
        return len(self.pos[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        position = self.pos[val].pop()
        lastone = self.nums[-1]

        self.nums[position] = lastone
        self.pos[lastone].add(position)
        self.pos[lastone].remove(len(self.nums)-1)

        self.nums.pop()
        
        if not self.pos[val]:
            del self.pos[val]
        return True


    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()