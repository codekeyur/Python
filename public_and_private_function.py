class Example:
    def __init__(self):
        self.x = 100
        self._y = 112    # Partially Private + Meaning Object can access the value
        self.__z = 130   # Complete Private = Meaning Object cannot access directly need to use a getMethod to access it

    def public_method(self): #now z can be access using this PUBLIC Method
        print(self.x)
        print(self._y)
        print(self.__z)
        self.__private_method() # Now the private method can be access using Public Method

    def __private_method(self):  #Private method cannot be access by Object
        print("Private Method")

object1 = Example()
print(object1.public_method())
print(object1.private_method())