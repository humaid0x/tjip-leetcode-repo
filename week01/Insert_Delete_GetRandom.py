class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.positions  = {}

    def insert(self, val: int) -> bool:
        if val in self.positions:
            return False
        self.positions[val] = len(self.nums)
        self.nums.append(val)
        return True 
        

    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False
        idx  = self.positions[val]
        last = self.nums[-1]
        
        self.nums[idx] = last
        self.positions[last] = idx
        
        self.nums.pop() 
        self.positions.pop(val)
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.nums)
