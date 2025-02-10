'''
Built-in class attributes:
Along with the other attributes, a Python class also contains some built-in class attributes
which provide information about the class.
1   __dict__      It provides the dictionary containing the information about the class namespace.
'''
class Student:    
    def __init__(self,name,id,age):    
        self.name = name;    
        self.id = id;    
        self.age = age  
  
    def display_details(self):    
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))  
  
s1 = Student("John",101,22) 
s2= Student("Doss" ,102,45)
   
print(s1.__dict__) 
print(s2.__dict__)
