from multiple_inheritance1 import ONE
from multiple_inheritance2 import TWO
class THREE(TWO):
    c=500
    def __init__(self,p,q,r):
        ONE.__init__(self,p)
        TWO.__init__(self,q)
        self.r=r
    def method3(self):
        print("im method 3")
obj3=THREE(1,4,6)
print(dir(obj3))

