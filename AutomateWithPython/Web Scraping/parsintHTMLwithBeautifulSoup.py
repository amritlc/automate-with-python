import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    elems = soup.select('#mediaTab_heading_1 > a > span > div:nth-child(1) > span')
    return elems[0].text.strip()




price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming-dp-1593275994/dp/1593275994/ref=mt_paperback?_encoding=UTF8&me=&qid=')

print('The price is ' + price)
