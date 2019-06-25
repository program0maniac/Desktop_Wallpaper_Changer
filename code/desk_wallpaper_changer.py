import ctypes
from bs4 import BeautifulSoup
import requests
import random
import os
import sys

def show_noConnection_mgs():
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, 'Internet is not Connected', 'Background Changer Warning', 0)

def get_imageLink(url):
    try:
        page = requests.get(url)
    except :
        show_noConnection_mgs()
        sys.exit()
    soup = BeautifulSoup(page.content, "html.parser")

    getDiv = soup.find('div', class_='content-main')
    getA = getDiv.find_all('a', class_='wallpapers__link')

    link = getA[random.randint(0, len(getA)-1)]['href']
    newLink = mainUrl + link

    secondPage = requests.get(newLink)
    secondSoup = BeautifulSoup(secondPage.content, "html.parser")
    secondDiv = secondSoup.find('div', class_='content-main')
    secondGetA = secondDiv.find('a', class_='gui-button gui-button_full-height')

    imageLink = secondGetA['href']
    return imageLink

def download(imgLink,fileName):
    filePath = "C:\\Users\\" + os.getlogin() + "\\Pictures\\" +fileName + ".jpg"
    resource = requests.get(imgLink)
    output = open(filePath,'wb')
    output.write(resource.content)
    output.close()

def change_walpaper(fileName):
    SPI_SETDESKWALLPAPER = 20
    imageFile = "C:\\Users\\" + os.getlogin() + "\\Pictures\\" +fileName + ".jpg"
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imageFile, 0)




mainUrl = "https://wallpaperscraft.com"
url = "https://wallpaperscraft.com/catalog/nature/date/1680x1050"
ran = random.randint(1,827)
if(ran!=1):
    url += "/page" + str(ran)


imgLink = get_imageLink(url)
imgName = "todays_choice"
download(imgLink,imgName)
change_walpaper(imgName)
