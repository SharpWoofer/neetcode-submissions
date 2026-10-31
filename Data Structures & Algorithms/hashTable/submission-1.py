from abc import get_cache_token
class Pair:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        # Initialize all capacity to null first
        self.map = [None] * capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        if self.get(key) == -1:
            # New insertion
            # If occupied, check next one
            while self.map[index] != None:
                index += 1
                index = index % self.getCapacity()
            self.map[index] = Pair(key, value)
            self.size += 1
            # Check if map is half full
            if self.getSize() >=  self.getCapacity() // 2:
                self.resize()
            return
        else:
            # Update value
            self.map[index].value = value
            return

    def hash(self, key: int) -> int:
        return key % self.getCapacity()

    def get(self, key: int) -> int:
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].value
            index += 1
            index = index % self.getCapacity()
        return -1

    def remove(self, key: int) -> bool:
        # if self.get(key) == -1: return False
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                
                # After setting self.map[index] = None and decrementing size:
                curr = (index + 1) % self.capacity
                while self.map[curr] is not None:
                    pair = self.map[curr]
                    self.map[curr] = None
                    self.size -= 1
                    self.insert(pair.key, pair.value)
                    curr = (curr + 1) % self.capacity
                return True
            index += 1
            index = index % self.getCapacity()
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        oldMap = self.map
        self.map = [None] * self.getCapacity() * 2
        self.size = 0
        self.capacity = self.getCapacity() * 2
        for pair in oldMap:
            if pair == None: continue
            else: self.insert(pair.key, pair.value)
