
import re

#Example1

txt = "Hi hello planet"
#Check if the string starts with 'hello':
x = re.search("^Hi hello", txt)   # search method returns true if match , otherwise false
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

# =======================================================================================

#Example2

txt = "hello planet"
#Check if the string starts with 'hello':
x = re.search("^hello", txt)   
# search method returns true if match , otherwise false
# ^ is used to match a string at the begining

if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")