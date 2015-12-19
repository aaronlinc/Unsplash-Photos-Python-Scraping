import requests
from bs4 import BeautifulSoup
import urllib
import re
import datetime
import time
import os

# Downloads the first 5 new images from unsplash.com

url = "https://unsplash.com/new"

req = requests.get(url)

soup = BeautifulSoup(req.content, "html.parser")

images = soup.find_all('div', {'class': 'photo'}, 'img')
author = soup.find_all('div', {'class': 'photo'}, 'alt')

#Returns list of five image urls from soupResult
def fiveNewImg(soupResult):
	newList = []
	i= 0
	while i < 5:
		newList.append(soupResult[i].img.get('src'))
		i = i + 1
	return newList

#Returns list five authors of a soupResult
def fiveAuthors(soupResult):
	newList = []
	i= 0
	while i < 5:
		newList.append(soupResult[i].img.get('alt'))
		i = i + 1
	return newList

img = fiveNewImg(images)
imgBy = fiveAuthors(author)

sep = '?'


for photo,by in zip(img,imgBy):
	millis = int(round(time.time() * 1000))
	millis = str(millis)
	photo = photo.split(sep,1)[0]
	urllib.urlretrieve(photo, by.encode('ascii', 'ignore') + millis + '.jpg')
	print photo