import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import urllib.request
from PIL import Image
# import downloadPath as dl
import shutil
import os
import time

# scraper = cloudscraper.create_scraper(browser='firefox',delay=10)

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

savePath= '/Users/dmitriytyutyunik/Desktop/'
mainLibrary='mangaFolderStorage'

overgear='https://mangamutiny.org/chapter/TbBg0YAs_/chap-55'
toonly='https://toonily.net/manga/global-martial-arts/chapter-65/'
omni='https://toonily.net/manga/omniscient-readers-point-of-view/chapter-35/'


def sendRequest(websiteAddress):
    
    response=requests.get(websiteAddress,headers=headers)
    return response.text

def beautifulSoupPrase(urlRequested):
    # time.sleep(6)
    # page = urllib.request.urlopen(urlRequested)
    data= BeautifulSoup(urlRequested,'html.parser')
    imgs = data.findAll("img", {"class": "wp-manga-chapter-img"})

    imgContainer={}
    for img in imgs:
        if img.has_attr('src'):
            src=img['src'].strip()
            label=img['id']
            imgContainer[label]=src
            # imgContainer.append(src)
            # print(label,':', src)
    path='/Users/dmitriytyutyunik/Desktop/mangaFolderStorage/test1/'

    for key,value in imgContainer.items():
        request=requests.get(value,stream=True)
        downloadAChapterManga(path+key+'.jpg',request)
    
 

    




def downloadAChapterManga(path,request):
    
        with open(path,'wb') as f:
            request.raw.decode_content=True
            # img=Image.open(request.raw)
            # img.save()
            shutil.copyfileobj(request.raw,f)
        del request
  
    

beautifulSoupPrase(sendRequest(omni))



def getVolChapterTitle(text):
    # \b to get rid of white space at the end
    if (re.search(' Vol',text)!=None):
         volChapterTitle=re.search(r'(\bVol[^-]*\b)',text)
    else:
        volChapterTitle=re.search(r'(\bChapter[^-]*\b)',text)

    return text[volChapterTitle.start():volChapterTitle.end()]

    #  volChapterTitle=re.search(r'(\bVol[^-]*\b)',text)
    #  return text[volChapterTitle.start():volChapterTitle.end()]

# Chapter 57 - Overgeared - MangaMutiny
def getMangaTitle(title):
    # Everything before Vol is the title
  chapterPageNumber=re.search(r'(\bChapter[^-]*)',title)
  print(chapterPageNumber)
    # some mangas dont have a Vol, so then we search for a Chapter
    # if (re.search('Chapter',title)!=None):
        # foundStartPoint=re.search(' Chapter',title).start()
    
    # return title[0:foundStartPoint]
    



def getChapterData(chapter):
    mangaContainerClass = chapter.find("div", {"class": "chapter--v__img"})
    
    imgs=mangaContainerClass.findAll('img')
    # print(imgs)
    
    mangaObj={}

    for img in imgs:
        if img.has_attr('src'):
            src=img['src'];
            title=img['title']
            # for title we will just get the page number
            chapterPageNumber=re.search(r'(\bpage[^-]*)',title)
            pageNumbers=title[chapterPageNumber.start():chapterPageNumber.end()].title()

            mangaObj[pageNumbers]=src
        else:
            print('issues with chapter')
        
    return mangaObj

def downloadAChapterManga(mangaTitle,chapterTitle,mangaObject):
    
    path = os.path.join(savePath, mainLibrary, mangaTitle, chapterTitle)
    
    print(path)
    # request=sendRequest(url, stream=True)
    
    # with open(path, 'wb') as file_path:
        # request.raw.decode_content=True
        # shutil.copyfileobj(request.raw,file_path)
        

    # for (key,index) in mangaObject.items():
        # request=sendRequest(index)
        # print(scraper.get(index).text)
        # print(request)
        # print(response.content)
    # im1 = Image.open(r"C:\Users\System-Pc\Desktop\flower1.jpg")  
  
    # save a image using extension 
    # im1 = im1.save("geeks.jpg") 

    # with open(path) as fpath:
    # for (key, index) in mangaObject.items():
            # fpath.write(index)
    #         # im1 = Image.open(index)  
    #         response=requests.get(index)
    #         with open(path, 'wb') as file:
    #             file.write(response.content)
            # print('key', key, 'index',index)
    




def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)



def main():

    # search=beautifulSoupPrase(sendRequest(latest))
    search=beautifulSoupPrase(sendRequest(url))
    if search!=404:
        print('it works')
    else:
        print('404 error')
    
