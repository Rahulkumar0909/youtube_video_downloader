import re

# write multiple inputs code from client OR can make extract url from file.
line = "https://www.youtube.com/watch?v=Mk3HvO3YEl8&t=2496s https://www.youtube.com/watch?v=ElOJReuu60g&t=4622s https://www.youtube.com/watch?v=2PjfpSgtuE8&t=6072s https://www.youtube.com/watch?v=vBUx9KZyoZM&t=7440s"

# Extracting urls
urls = []
# gives whole url from any string
urls = re.findall(
    'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
# number of urls.
num = len(urls)
print(urls[0:num+1])
# got the list of urls from client.

print("\n\n")

# change url domain name and update in different list.
for url in range(0, num):
    replaced_url = []
    replacing_url = re.sub(r"youtube", "youtubepp", urls[url])
    replaced_url.append(replacing_url)
    print(replaced_url)
