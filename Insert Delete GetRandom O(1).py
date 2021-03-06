import random

class RandomizedSet(object):

    def __init__(self):
        self.nums = [] 
        self.pos = {}
        
    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False
        

    def remove(self, val):
        if val in self.pos:
            idx = self.pos[val]
            last =  self.nums[-1]
            
            self.nums[idx] = last
            self.pos[last] = idx
            self.nums.pop()
            self.pos.pop(val)
            return True
        return False
            
    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]
