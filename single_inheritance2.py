from single_inheritance1 import ONE
class TWO(ONE):
    b=200
    def __init__(self,p,q):
        super().__init__(p)
        self.q=q
    def method2(self):
        print("IM METHOD 2")
        
obj1=TWO(10,20)
print(dir(obj1))  