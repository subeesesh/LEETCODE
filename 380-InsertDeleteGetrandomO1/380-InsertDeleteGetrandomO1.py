# Last updated: 5/29/2026, 11:55:57 AM
class RandomizedSet:

    def __init__(self):
        self.randset=set()

    def insert(self, val: int) -> bool:
        if val in self.randset:
            return False
        else:
            self.randset.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.randset:
            return False
        else:
            self.randset.remove(val)
            return True

    def getRandom(self) -> int:
        l=list(self.randset)
        return random.choice(l)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()