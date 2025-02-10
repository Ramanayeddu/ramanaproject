#Negative Indexing:

#Negative indexing is useful for accessing elements from the end of the list. 

#The last element has an index of -1, the second last element -2, and so on.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements starting from index -2
# to end of list
b = a[-2:]
print(b)

#Example2

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements starting from index 0 
# to index -3 (excluding 3th last index)
c = a[:-3]
print(c)

#Example3

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get elements from index -4
# to -1 (excluding index -1)
d = a[-4:-1]
print(d)

#Exaple4

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get elements from index -4
# to -1 (excluding index -1)
d = a[-4:-1]
print(d)

#Example5

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get elements from index -4
# to -1 (excluding index -1)
d = a[-4:-1]
print(d)


#Example6

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get every 2nd elements from index -8

# to -1 (excluding index -1)
e = a[-8:-1:2]
print(e)


#Example7
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get the entire list using negative step
b = a[::-1]
print(b)