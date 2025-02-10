#dictinary

#1. elements are enclosed in  { }

#2. it has key value  pair <k,v> k is key(immutable) and v is value it is mutable


#passportno=========>name of person

#pancard ===========> name of person

#for a given vechile number , we can get all details .


staff={"name" : "doss",
        "age" :  45 ,
        "loc" : "Bangalore"}

print(type(staff))
print(staff)


#Example2

staff={"name" : "doss",
        "age" :  45 ,
        "loc" : "Bangalore"}

print(type(staff))
print(staff)
# print only keys
print("\n")
for i in staff:
    print(i)
# print only keys
print("\n")
for i in staff.keys():
    print(i)
# To print values
print("\n")
for i in staff.values():
    print(i)