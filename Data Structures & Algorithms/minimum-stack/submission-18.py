class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(not self.min_stack):
            self.min_stack.append(val)
        elif(self.min_stack and val<=self.min_stack[-1]):
            self.min_stack.append(val)
        #else:
            #self.min_stack.pop()

    def pop(self) -> None:
        if self.min_stack:
            popped = self.stack.pop()
            if popped == self.min_stack[-1]:
                self.min_stack.pop()            
        else:
            self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            print(self.min_stack[-1])
            return self.min_stack[-1]