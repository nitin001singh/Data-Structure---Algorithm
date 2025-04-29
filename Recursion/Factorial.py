class Factorial:
    def answer(self, num):
        if num == 0:
            return 1
        
        return num * self.answer(num - 1)    

result = Factorial().answer(5)
print(result)