'''
Assignment 1


Syntax : map(fn, iterable)   iterable means  list, tuple , dictionary , sequence etc

      map  function applies fn  to each element of the iterable and returns an object

x=[2,3,4,5]

i need output say  y=[4,5,6,7]
'''
x=[2,3,4,5]
y=[]
for i in x:
    va=i+2
    y.append(va)
print(x)
print(y)

#Method 2 :

x=[2,3,4,5]
y=map(lambda a:a+2, x)
