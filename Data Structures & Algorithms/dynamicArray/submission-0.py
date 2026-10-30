class DynamicArray:
    
    def __init__(self, capacity: int):
        self.end_element = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity(): self.resize()
        self.set(self.end_element,n)
        self.end_element += 1

    def popback(self) -> int:
        temp = self.arr[self.end_element - 1]
        self.end_element -= 1
        return temp

    def resize(self) -> None:
        temp = [0] * 2 * self.getCapacity()
        for i in range(self.getSize()):
            temp[i] = self.arr[i]
        self.arr = temp

    def getSize(self) -> int:
        return self.end_element
    
    def getCapacity(self) -> int:
        return len(self.arr)