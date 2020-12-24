import requests
from bs4 import BeautifulSoup
import re


#Specific 
url='https://manganelo.com/chapter/cd918233/chapter_90'
latest='https://manganelo.com/genre-alls'

def sendRequest(websiteAddress):
    
    response=requests.get(websiteAddress)
    return response.text

def beautifulSoupPrase(urlRequested):
    
    data= BeautifulSoup(urlRequested,'html.parser')
    # print(data)
    mydivs = data.find("div", {"class": "container-chapter-reader"})
    mydivsSet = set(data.find("div", {"class": "container-chapter-reader"}))
    mangaTitles=[]
    mangaImages=[]
    # print(mydivs)

    print(len(mydivs.contents))

    for items in range(len(mydivs.contents)):
        print(mydivs.contents[items])

    # for div in mydivs:
        # print(mydivs.contents[div])
    # print(mydivs.img)
    # print(mydivs.img)
    # print(mydivsSet)
    
    # print(mydivsSet['img'])
    # print(mydivs)
    # print(mydivs.contents[1])
    # for a in range(mydivs.length):
        # print(a)
        
    
    # print(mydivs)




    # if '404 Not Found' in data.title.text:
    #     return (404)
    # else:
    #     return showTitle(data.title.text)
    
beautifulSoupPrase(sendRequest(url))


def showTitle(string):
    word=re.search(' - Manganelo',string)
    foundStartPoint=word.start()
    return string[0:foundStartPoint]
    # print(string[0:foundStartPoint])


def main():

    # search=beautifulSoupPrase(sendRequest(latest))
    search=beautifulSoupPrase(sendRequest(url))
    if search!=404:
        print('it works')
    else:
        print('404 error')
    
# main()

def findAllImages(urlRequested,manga):
    pass




# print(response.content)
# print(response.json)

# soup = BeautifulSoup(text, 'html.parser')
# title_tag='panel-content-genres'
# print(soup.title_tag)


# mydivs = soup.findAll("div", {"class": "panel-content-genres"})
