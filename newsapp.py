import json
import requests
def getparams():
    global cntry
    global cat
    global lan
    cntry = str(input("Enter country code: "))
    cat = str(input("Enter category: "))
    lan = str(input("Enter language code: "))
def getnews(c = " ", ca = " ", l = "en"):
    url = (f'country={c}&'
           f'category={ca}&'
           f'language={l}&'
           'apiKey=your api key')
    main = 'https://newsapi.org/v2/top-headlines?'
    response = requests.get(main, params = url)
    r = response.json()
    arts = r["articles"]
    titles = []
    for i in arts:
        titles.append(f"Author: {i["author"]}")
        titles.append(f"Title: {i["title"]}")
        titles.append(f"Url: {i["url"]}")
        titles.append(f"Description: {i["description"]}\n")
    for j in titles:
           print(j)
def main():
    getparams()
    getnews(cntry, cat, lan)
main()

