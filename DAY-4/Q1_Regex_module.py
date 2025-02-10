'''
import re  
^    : To match at the begining
$    : To match at the end
.    : Any character (except newline character) 
[]   :	A set of characters
{}   :	Exactly the specified number of occurrences
*    :	Zero , one or  more occurrences  >=0
+    :  1 or more occurrences            >=1
?    :  0 or 1                          
'''

import re
txt = "hello planet"
#Check if the string starts with 'hello':
x = re.search("^hello", txt)   # search method returns true if match , otherwise false
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")