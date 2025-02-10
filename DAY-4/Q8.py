import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.search("he.+o", txt)
if x:
   print("There is a match ")
else:
   print("There is no match  ")
