# Define the private data/value inside the class and access it
#Change the value only using the method inside the class
class Ec2:
    def __init__(self):
        self.name = "Private Instance"
        self.id = "a24124ffef"
        self.__state = "Running"

    def get_instance(self):
        return self.__state

    def set_instance_state(self, state):
        self.__state = state

instance1 = Ec2()
print(instance1.get_instance())

instance1.set_instance_state("Stop")
print(instance1.get_instance())