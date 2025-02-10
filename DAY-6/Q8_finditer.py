'''
python regex finditer() function to find all matches in a string and 
return an iterator that yields match objects.
The following example uses the finditer() function to search for all vowels in a string:
'''
import re

s = 'Readability counts.'

pattern = r'[aeoui]'

matches = re.finditer(pattern, s)
for match in matches:
    print(match)