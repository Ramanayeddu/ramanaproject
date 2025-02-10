'''
tuple :

it is similar to list except

1. elements can not be modified or added or deleted

2. elements are enclosed in  ()

'''
#Exam1

score=()
print(type())

#Eaxm 2:

marks=(23, 45, 67)

marks[0]= 55  # can not be modified

#example 3

score=()
print(type(score))
marks=(23,45,67)
print(marks)
print(type(marks))
#marks[0]=87 # it is immutable can not be modified or added or deleted
#since tuple items can not be modified , we can convert into list, change it 
# again put back to tuple
marks=list(marks)

print(type(marks))
marks[0]=90
marks=tuple(marks)
print(marks)