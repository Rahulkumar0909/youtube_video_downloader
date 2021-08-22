import re

#line = "This is my tweet check it out http://example.com/blah hi https://www.youtube.com/"

# write multiple inputs code from client OR can make extract url from file.
line = "https://www.youtube.com/watch?v=Mk3HvO3YEl8&t=2496s https://www.youtube.com/watch?v=ElOJReuu60g&t=4622s https://www.youtube.com/watch?v=2PjfpSgtuE8&t=6072s https://www.youtube.com/watch?v=vBUx9KZyoZM&t=7440s"

# gives only domain name.
# urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)  # ?? research

# gives whole url from any string
urls = []
urls = re.findall(
    'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
# number of urls.
num = len(urls)
print(urls[0:num+1])
# got the list of urls from client.

# change url domain name and update in different list.
for url in range(0, num+1):
    replaced_url = []
    number = 0
    replacing_url = re.sub(r"youtube", "youtubepp", urls[number])
    replaced_url.append(replacing_url)
    number += number

print(replaced_url)


#s = "https://www.youtube.com/watch?v=Mk3HvO3YEl8&t=2496s"

# not good in this case because it replaces all e with epp
# replace = re.sub('[e]', 'epp', s)

#replace = re.sub(r"youtube", "youtubepp", s)

# print(f'{replace}')

# create a file with changed urls.
