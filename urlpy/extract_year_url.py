with open("url_list.txt","r") as f:
    url_list = f.readlines()

r_url_list = []
for url in url_list:
    if "2011" in url:
        r_url_list.append(url)

with open("2011url.txt","w") as f:
    for url in r_url_list:
        f.write(url)