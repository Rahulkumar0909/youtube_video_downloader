import re

#line = "Cats are smarter than dogs"
line = "https://www.youtube.com/watch?v=Mk3HvO3YEl8&t=2496s"

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group(1) : ", searchObj.group())
else:
    print("Nothing found!!")

'''
import re

text = "https://www.youtube.com/watch?v=Mk3HvO3YEl8&t=2496s"

found = re.findall('youtube\.', text)

print(f"{found}")
'''
