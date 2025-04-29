class Power:
    def answer(self, num, p):
        if p == 0:
            return 1
        
        return num * self.answer(num, p-1)
        
result = Power().answer(7,4)
print(result)