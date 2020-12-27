import shutil
import os
from PIL import Image


savePath= '/Users/dmitriytyutyunik/Desktop/'
mainLibrary='mangaFolderStorage'

def createMainLibrary():
    path = os.path.join(savePath, mainLibrary)
    try:  
        os.mkdir(path)  
        print('created the folder')
    except OSError as error:  
        print(error)   


def createMangaTitle(mangaTitle):
    path = os.path.join(savePath, mainLibrary, mangaTitle)
    try:  
        os.mkdir(path)  
        print('created the folder')
    except OSError as error:  
        print(error) 

def createChapterFolder(mangaTitle,chapterTitle):
    path = os.path.join(savePath, mainLibrary, mangaTitle, chapterTitle)
    try:  
        os.mkdir(path)  
        print('created the folder')
    except OSError as error:  
        print(error) 


def downloadAChapter(mangaTitle,chapterTitle,mangaObject):
    path = os.path.join(savePath, mainLibrary, mangaTitle, chapterTitle)
    
    for (key, index) in mangaObject.items():
        print('key', key, 'index',index)
        image1 = Image.open(r'path where the image is stored\file name.png')
        im1 = image1.convert('RGB')
        im1.save(r'path where the pdf will be stored\new file name.pdf')
    # pass

def runner(mangaTitle,mangaObject):
    createMainLibrary()
    createMangaTitle(mangaTitle)
    # downloadAChapter(mangaObject)

# runner
