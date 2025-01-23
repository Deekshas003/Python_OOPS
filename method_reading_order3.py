from method_reading_order1 import A
from method_reading_order2 import B
class C(A,B):
    def method3(self):
        print("Im a method3 from class C")
obj=C()
print(dir(C))
obj.method()
# here only 1 metjod occurs, but which method , from A or B ?
#diamond abiquity happens only in java but in python we have method_readding 