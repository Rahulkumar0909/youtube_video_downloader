with open('input.txt', 'r') as file:
    urlStr = file.read()
print(urlStr)

'''
# Better can sak for path in UI

from pathlib import Path
countriesStr=Path('countries.txt').read_text()
print(countriesStr)
'''
