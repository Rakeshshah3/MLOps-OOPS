# initiate a class 
class employee:
    #special function/ magic method / dunder method - Constructor
    def __init__(self):
        print("Started executing attributes")
        self.id=3
        self.designation="SDE"
        self.salary=50000
        print("Attributes/data have been initiated")

    def travel(self,destination):
        print("This travel function was called manually")
        print(f"The employee is going to {destination}")

# create an obj/instance of the class 
sam=employee()
# print(sam.salary)
# print(sam.id)
# sam.travel("Panipat")        
print(type(sam))