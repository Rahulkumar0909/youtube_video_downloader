import re

# Take text from file and save in variable.
with open('input.txt', 'r') as file:
    urlStr = file.read()

# Extracting urls
urls = []
# gives whole url from any string
urls = re.findall(
    'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', urlStr)
# number of urls.
num = len(urls)
print(urls[0:num+1])
# got the list of urls from client.

print("\n\n")


# change url domain name and update in different list.
replaced_url = []
for url in range(num):
    replacing_url = re.sub(r"youtube", "youtubepp", urls[url])
    replaced_url.append(replacing_url)

print(replaced_url)


# Creates a new empty filefile
with open('updated_url.txt', 'w') as ufile:
    ufile.writelines("% s\n" % data for data in replaced_url)
    ufile.close()
