'''
List Comprehension in Python
List comprehension is a way to create lists using a concise syntax.
It allows us to generate a new list by applying an expression to each item 
in an existing iterable (such as a list or range). This helps us to write cleaner, 
more readable code compared to traditional looping techniques.

syntax:
newlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged.
'''



#Example 1
score=[23,45,67,89,12]
pmarks=[ i  for i in score if i>=50]
fmarks=[ i   for i in score if i<50]
print(score)
print(pmarks)
print(fmarks)


#Example2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#Example3
#create two list evenos and oddnos from range(10) using list comprehension

evenos=[x for x in range(10) if x % 2 ==0]
oddnos=[x for x in range(10) if x % 2 !=0]
print(evenos)
print(oddnos)


#Example5
#create list cel contains temp in celcius for the corresponding elements in fah


fah=[100,101,102,103,104,105]

cel = [ (x-32)/1.8  for x in fah  ] 

print(fah)
print(cel)

