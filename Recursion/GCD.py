class GCD:
    def answer(self, num1, num2):
        if num2 == 0:
            return num1
        
        return self.answer(num2, num1%num2)
        
        
        
result = GCD().answer(18,48)
print(result)