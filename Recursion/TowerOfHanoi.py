# TC : O(2^n)
# SC : O(n)
class TowerOfHanoi:
    def answer(self, n, source, helper, destination):
        if n == 0:
            return 
        
        self.answer(n-1, source, destination, helper)
        print("Disk {} moving from {} to {}".format(n , source, destination))
        self.answer(n-1, helper, source, destination)
        
result = TowerOfHanoi().answer(3, 'A', 'B', 'C')
print(result)