baseUrl = "https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89"
pref = "https://wiki.52poke.com"

from bs4 import BeautifulSoup
import requests

req = requests.get(baseUrl)
encodedText = req.text.encode("utf-8")
soup = BeautifulSoup(encodedText, "html.parser")

for table in soup.find_all("table", class_= ["roundy", "eplist"]):
    for tr in table.find_all("tr"):
        for td in tr.find_all("td"):
            link = td.find("a")
            if link:
                subLink = pref + link["href"]
                subReq = requests.get(subLink)
                subEncodedText = subReq.text.encode("utf-8")
                subSoup = BeautifulSoup(subEncodedText, "html.parser")
                for img in subSoup.find_all("img", {"height" : "300"}):
                    image_url = "http:" + img["data-url"]
                    img_data = requests.get(image_url).content
                    image_name = image_url.split("/")[-1]
                    print image_name
                    with open(image_name, 'wb') as handler:
                        handler.write(img_data)
                    break
                break
