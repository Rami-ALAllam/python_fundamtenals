class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        for i in nums:
            self.result += i
        self.result += num
        return self
    def subtract(self, num, *nums):
        for i in nums:
            self.result -= i
        self.result -= num
        return self

md = MathDojo()

x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	

y = md.add(2,3,6).add(1).add(3,8,4,7,5).result
print(y)

z = md.subtract(3,2,5,8,1).subtract(3).subtract(3,2,1,4,5).result
print(z)
