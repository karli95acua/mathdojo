# ACTIVIDAD MATH DOJO
class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for additional_num in nums:
            self.result += additional_num
        print(self.result)
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for additional_num in nums:
            self.result -= additional_num
        print(self.result)
        return self


prueba1 = MathDojo()
prueba1.add(20).add(2).add(2,5,1).subtract(3,2)
print("----------------SIG----------------")
prueba2 = MathDojo()
prueba2.add(50).add(90).add(20,50,10).subtract(30,20)
print("----------------SIG----------------")
prueba3 = MathDojo()
prueba3.add(100).add(5).add(4,3,2).subtract(1,20)
print("----------------FINAL----------------")



