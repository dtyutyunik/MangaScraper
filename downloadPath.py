import shutil
import os

savePath= '/Users/dmitriytyutyunik/Desktop/mangaFolderStorage/'


# creates the path where we download
def get_download_path(seriesName, episodeNum):
    return savePath+seriesName+'/'+episodeNum+'/'
