class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.kv = collections.defaultdict(int)

    def insert(self, val):
        if val in self.kv: return False
        self.kv[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        if val in self.kv:
            index, last = self.kv[val], self.nums[-1]
            self.kv[last], self.nums[index] = index, last
            self.kv.pop(val)
            self.nums.pop()
            return True
        return False

    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]