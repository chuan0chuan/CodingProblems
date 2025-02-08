
class NumberContainers:
    def __init__(self):
        self.index_map = {}  # Stores index → number
        self.number_map = defaultdict(SortedSet)  # Stores number → sorted set of indices

    def change(self, index: int, number: int) -> None:
        if index in self.index_map:
            old_number = self.index_map[index]
            self.number_map[old_number].discard(index)  # Remove from old number set
        
        self.index_map[index] = number  # Update mapping
        self.number_map[number].add(index)  # Add index to new number set

    def find(self, number: int) -> int:
        if not self.number_map[number]:  # No indices for this number
            return -1
        return next(iter(self.number_map[number]))  # Get the smallest index

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)