import urllib.request as req
import bs4


def GetData(url):
    url = "https://www.ptt.cc/bbs/Gossiping/index.html"
    request = req.Request(url, headers={
        "cookie": "over18=1",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)

    nextlink = root.find("a", string="‹ 上頁")
    return nextlink["href"]

class main():
    pageUrl = "https://www.ptt.cc/bbs/Gossiping/index.html"
    count = 0
    while count < 5:
        pageUrl = "https://www.ptt.cc" + GetData(pageUrl)
        count += 1
