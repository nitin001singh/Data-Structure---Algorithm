class MinStack:
    def __init__(self):
        self.arr = []
        
        
    def push(self, val):
        self.arr.append(val)
        print(self.arr)
        

    def pop(self):
        self.arr = self.arr[:-1]
        print(self.arr)
        return self.arr
        

    def top(self):
        print(self.arr[-1])
        return self.arr[-1]
        

    def getMin(self):
        print(min(self.arr))
        return min(self.arr)
        
        
        
    
     
# minStatck = MinStack()
# minStatck.push(-2)
# minStatck.push(0)
# minStatck.push(-3)
# minStatck.getMin()
# minStatck.pop()
# minStatck.top()
# minStatck.getMin()

# print([minStatck])


# [null,null,null,null,-3,null,0,-2]