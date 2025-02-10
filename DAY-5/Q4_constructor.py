'''
More than One Constructor in Single class:

Let's have a look at another scenario, what happen if we declare the two same constructors in the class.
'''
class Student:  
    def __init__(self):  
        print("The First Constructor")  
    def __init__(self):  
        print("The second contructor")  
  
st = Student()  