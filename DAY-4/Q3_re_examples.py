
import re
txt = "Muruga doss"
#Check if the string if ends with doss :
# $ symbol is used to match at the end
x = re.search("doss$", txt)   
# search method returns true if match , otherwise false
if x:
  print("Yes, the string ends  doss")
else:
  print("No  ")
# =======================================================================================
import re
txt = "welcome helo planet"
#Search for a sequence that starts with "he", followed by two (any) characters,
#and an "o":
x = re.search("he..o", txt)
if x:
   print("Match")
else:
   print("No match")  