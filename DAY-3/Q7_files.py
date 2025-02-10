#Lab 2 : Reading names.txt

# read() method reads entire file

# readline() method reads single line

# read(x)  method reads x bytes from the file


f=open("names.txt" ) # r mode is the default 
print(f.read())   # read() reads entire file 

f=open("names.txt" ) # r mode is the default 
print(f.readline())   # readline() reads oneline at  a time 
f.close()

f=open("names.txt" ) # r mode is the default 
print(f.read(3))   # read(3) reads three bytes 
f.close()