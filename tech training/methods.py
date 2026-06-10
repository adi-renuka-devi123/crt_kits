# prg 1 using the setter & getter methods
"""class Customer:
    def __init__(self):
        pass
    def set_id(self,id):
        self.id=id
    def set_name(self,name):
        self.name=name
    def set_age(self,age):
        self.age=age
    def get_id(self):
        print(f"id is {self.id}")
    def get_name(self):
        print(f"name is {self.name}")
    def get_age(self):
        print(f"age is {self.age}")
C1=Customer()
C1.set_id(123)
C1.set_name('amith')
C1.set_age(21)
C1.get_id()
C1.get_name()
C1.get_age()
"""
# prg 2 class method without parameter
"""class Mobile:
    @classmethod
    def show_model(cls):
        print("RealMe x")
realme=Mobile()
Mobile.show_model() """

# prg 3 static method without parameter
class Mobile:
    @staticmethod
    def show_model():
        print("RealMe x")
realme=Mobile()
Mobile.show_model()
