import requests
from bs4 import BeautifulSoup
import re
import downloadPath as dl

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


#Specific 
kengan='https://manganelo.com/chapter/cd918233/chapter_90'
kengan1='https://manganelo.com/chapter/utua281931572859970/chapter_7'
latest='https://manganelo.com/genre-alls'
masarou='https://manganelo.com/chapter/dc919868/chapter_63'
vinland='https://manganelo.com/chapter/vinland_saga/chapter_178'
solo='https://manganelo.com/chapter/pn918005/chapter_132'
simplifed='https://manganelo.com/chapter/jb918021/chapter_154'
overgeared='https://manganelo.com/chapter/lr922610/chapter_59';

# dled

# https://s8.mkklcdnv8.com/mangakakalot/d1/dc919868/vol7_chapter_63_naruse_and_yamato/1.jpg
# https://s8.mkklcdnv8.com/mangakakalot/c1/cd918233/chapter_90_perfected/1.jpg

# https://bu.mkklcdnbuv1.com/mangakakalot/v1/vinland_saga/vol25_chapter_178_sailing_west_part_12/1.jpg

# https://s8.mkklcdnv8.com/mangakakalot/p1/pn918005/vol2_chapter_132/1.jpg
# https://s8.mkklcdnv8.com/mangakakalot/j1/jb918021/chapter_154_scp368/1.jpg
# https://s8.mkklcdnv8.com/mangakakalot/l2/lr922610/chapter_59/1.jpg 



# actual website

# https://bu.mkklcdnbuv1.com/mangakakalot/m1/masuraou/vol7_chapter_63_naruse_and_yamato/1.jpg

# https://bu.mkklcdnbuv1.com/mangakakalot/k1/kengan_omeg/chapter_90_perfected/1.jpg

# https://bu.mkklcdnbuv1.com/mangakakalot/v1/vinland_saga/vol25_chapter_178_sailing_west_part_12/1.jpg

# https://bu.mkklcdnbuv1.com/mangakakalot/s2/solo_leveling/vol2_chapter_132/1.jpg
# https://bu.mkklcdnbuv1.com/mangakakalot/o2/oversimplified_scp/chapter_154_scp368/1.jpg
# https://bu.mkklcdnbuv1.com/mangakakalot/l2/lr922610/chapter_59/1.jpg

def sendRequest(websiteAddress):
    
    response=requests.get(websiteAddress,headers=headers)
    return response.text

def beautifulSoupPrase(urlRequested):
    
    data= BeautifulSoup(urlRequested,'html.parser')
    print(data.prettify())
    # creates the mainLibrary on desktop where the files will be stored
    # dl.createMainLibrary()

    # this function returns the title of the manga
    mangaTitle=getMangaTitle(data.title.text)
    # print(mangaTitle)
    
    # this function creates the folder holding the manga
    # dl.createMangaTitle(mangaTitle)

    chapterVolTitle=getVolChapterTitle(data.title.text)
    # print(chapterVolTitle)
    # dl.createChapterFolder(mangaTitle,chapterVolTitle)
    # this function returns the Vol/Chapter Title


    # returns an Object with key beign Page #, and value being JPG for that page
    chapterData=getChapterData(data)
    # print(chapterData)
    # dl.downloadAChapter(chapterData)
    


    # return getChapterData(data)

    # if '404 Not Found' in data.title.text:
    #     return (404)
    # else:
    #     return showTitle(data.title.text)




def getVolChapterTitle(text):
    # \b to get rid of white space at the end
    if (re.search(' Vol',text)!=None):
         volChapterTitle=re.search(r'(\bVol[^-]*\b)',text)
    else:
        volChapterTitle=re.search(r'(\bChapter[^-]*\b)',text)

    return text[volChapterTitle.start():volChapterTitle.end()]

    #  volChapterTitle=re.search(r'(\bVol[^-]*\b)',text)
    #  return text[volChapterTitle.start():volChapterTitle.end()]


def getMangaTitle(title):
    # Everything before Vol is the title

    # some mangas dont have a Vol, so then we search for a Chapter
    if (re.search(' Vol',title)!=None):
        foundStartPoint=re.search(' Vol',title).start()
    else:
        foundStartPoint=re.search(' Chapter',title).start()
    
    return title[0:foundStartPoint]
    



def getChapterData(chapter):
    mangaContainerClass = chapter.find("div", {"class": "container-chapter-reader"})
    
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
            # print('pageNumbers: ', pageNumbers, ' src: ', src)
            mangaObj[pageNumbers]=src
        else:
            print('issues with chapter')
        
    return mangaObj




beautifulSoupPrase(sendRequest(overgeared))




def main():

    # search=beautifulSoupPrase(sendRequest(latest))
    search=beautifulSoupPrase(sendRequest(url))
    if search!=404:
        print('it works')
    else:
        print('404 error')
    
