from multilevel_inheritance2 import TWO
class THREE(TWO):
    c=500
    def __init__(self,p,q,r):
        super().__init__(p,q)
        self.r=r
    def method3(self):
        print("im method 3")
obj2=THREE(1,4,6)
print(dir(obj2))

