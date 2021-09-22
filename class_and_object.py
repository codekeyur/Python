#    Creating Class
#    What is __init__ ? So, it is use to initilizer the variables inside class so
#    its call constructor or initilizer and you can only use the one __init__ method in class
#    Why we us __ at starting and ending point, it is means that it is interanlly
#    define and we cannot use/call that method anywhere in the code.It is automatically
#    called when we create an object
  
#    What is self ? So, it is varible that refers to the current class and will be called when we call object
class Student:
    def __init__(self):

    #  self.name = "keyur"  attributes of class
     self.age = 25
     self.marks = 820

#    Methods of class which basically a function inside the class
    def talk(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        
#    Executing/Utilizing Class by Creating Object/Instance
s1 = Student()
s1.name = "Keyur"
#    Using the object we called the methods from the class
s1.talk()