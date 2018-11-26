import random

class RandomizedCollection(object):

    def __init__(self):
        self.vals = []
        self.map = collections.defaultdict(set)
        

    def insert(self, val):
        self.vals.append(val)
        self.map[val].add(len(self.vals) - 1)
        return len(self.map[val]) == 1
        

    def remove(self, val):
        if self.map[val]:
            idx = self.map[val].pop()
            last = self.vals[-1]
            self.vals[idx] = last
            if self.map[last]:
                self.map[last].add(idx)
                self.map[last].discard(len(self.vals) - 1)
            self.vals.pop()
            return True
        return False 

    def getRandom(self):
        #return random.choice(self.vals)
        return self.vals[random.randint(0, len(self.vals) - 1)]
