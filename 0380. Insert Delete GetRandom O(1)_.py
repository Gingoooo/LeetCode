class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        last, idx = self.list[-1], self.dic[val]
        self.list[idx], self.dic[last] = last, idx
        del self.list[-1]
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        import random
        idx_random = random.choice(self.list)
        return idx_random


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()