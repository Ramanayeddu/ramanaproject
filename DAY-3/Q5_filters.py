
#filter(fn , iterable)

#this filter function applies fn to each element of the iterable and returns element for which the cond is True

marks=[12,45,56,78,09]

pmarks=filter(lambda a: a>=50 , marks)

print(list(pmarks))


#Example

marks=[12,45,56,78,9]
pmarks=filter(lambda a: a>=50 , marks)
fmarks=filter(lambda a: a<50  , marks)
print(list(pmarks))
print(list(fmarks))

#example

marks=[12,45,56,78,9]
pmarks=filter(lambda a: a>=50 , marks)
fmarks=filter(lambda a: a<50  , marks)
print(list(pmarks))
print(list(fmarks))