class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        if (self.size==self.capacity):
            self.resize()
            self.set(self.size,n)
        else:
            self.set(self.size,n)
        self.size+=1


    def popback(self) -> int:
        temp = self.arr[self.size-1]
        self.arr[self.size-1] = 0
        self.size-=1
        return temp

        

    def resize(self) -> None:
        self.capacity*=2
        new_array = self.arr
        self.arr = [0]*self.capacity
        for i in range(0,len(new_array)):
            self.arr[i] = new_array[i]

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity